import heapq
import asyncio

from ..models import Group
from ..models import Expense
from ..models import ExpensePayingUser
from ..models import ExpenseOwingUser
from collections import defaultdict
from ..models import Transaction
from .EmailServices import send_expense_notification

class Record:
    def __init__(self, user, amount):
        self.amount = amount
        self.user = user

    def __gt__(self, other):
        return self.amount > other.amount


class GroupSettleUpService:
    def __init__(self, group_id):
        self.group_id = group_id

    async def settle_up_greedy(self):
        current_group = Group.objects.get(id=self.group_id)
        if current_group is None:
            raise ValueError("not found")
        expenses = Expense.objects.filter(group=current_group)
        expense_paying_users = []
        expense_owing_users = []

        for g_expense in expenses:
            paying_users = ExpensePayingUser.objects.filter(expense=g_expense)
            owing_users = ExpenseOwingUser.objects.filter(expense=g_expense)
            expense_paying_users.extend(paying_users)
            expense_owing_users.extend(owing_users)



        # MINIMISE THE TRANSACTIONS
        extra_money = defaultdict()


        for paying_user in expense_paying_users:
            user = paying_user.user
            amount = paying_user.amount
            extra_money[user] += amount

        for owing_user in expense_owing_users:
            user = owing_user.user
            amount = owing_user.amount
            extra_money[user] -= amount

        pay_money_heap = []
        owe_money_heap = []
        # Both are max heaps
        # Minimising transactions

        transactions = []

        for user, amount in extra_money.items():
            record = Record(user, amount)
            if amount < 0:
                heapq.heappush(owe_money_heap, (amount, record))
            elif amount > 0:
                heapq.heappush(pay_money_heap, (-amount, record))

        while len(pay_money_heap) and len(owe_money_heap):
            paying_record = heapq.heappop(pay_money_heap)
            owing_record = heapq.heappop(owe_money_heap)
            record = None
            if abs(paying_record[0]) > abs(owing_record[0]):
                # 10rs and you are paying someone who needs 4 rs
                transactions.append(Transaction(paying_record[1].user,
                                              owing_record[1].user, abs(owing_record[1].amount)))
                amount_left = abs(paying_record[1].amount) - abs(owing_record[1].amount)
                record = Record(paying_record[1].user, amount_left)
                heapq.heappush(pay_money_heap, (-amount_left, record))
            else:
                # paying user has lesser money than owing user
                # sending 6 rupees to someone who needs 10 right
                transactions.append(Transaction(paying_record[1].user, abs(paying_record[1].amount)))
                amount_left = abs(owing_record[1].amount) - abs(paying_record[1].amount)
                record = Record(owing_record[1].user, amount_left)
                heapq.heappush(owe_money_heap, (amount_left, record))

        email_tasks = [
            send_expense_notification(user.email, transactions[user][0]) for user in expense_owing_users
        ]
        await asyncio.gather(*email_tasks)

        return transactions





