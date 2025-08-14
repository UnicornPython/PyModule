
# python 标准库中提供了单元测试的框架 unittest

import unittest
from unittest.mock import patch
from bank_account import BankAccount

# 测试类时需要继承 unittest.TestCase
class TestBankAccount(unittest.TestCase):

    # 在类级别，执行所有测试前执行一次
    @classmethod
    def setUpClass(cls):
        print("setup class")

    # 在类级别，执行所有测试后执行一次
    @classmethod
    def tearDownClass(cls):
        print("tear down class")

    # 每次测试前都会执行
    def setUp(self):
        self.account = BankAccount(100)

    # 每次测试后都会执行
    def tearDown(self):
        print("tear down")

    
    def test_create_account(self):
        self.assertIsInstance(self.account, BankAccount)

        with self.assertRaises(ValueError):
            BankAccount(-100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150,
                         "Balance should be 150 after depositing 50")
        self.account.deposit(-50)


    def test_withdraw(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50,
                         "Balance should be 50 after withdrawing 50")
        self.account.withdraw(-50)



    def test_get_interest_rate(self):
        # 使用 patch 函数来模拟 requests.get
        with patch("BackAccount.requests.get") as mock_get:
            # 指定 模拟数据的详细信息
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {"rate": 0.01}

            # 判定请求之后的代码正确性
            self.assertEqual(self.account.get_interest_rate(), 0.01)



