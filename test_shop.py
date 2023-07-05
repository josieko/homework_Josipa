from unittest import TestCase, mock
from shop import NoFundsError, sim_shop, MaxTriedError

import unittest


class TestSimShop(TestCase):
    @mock.patch('builtins.input', side_effect=['Vegan mango cheesecake', 'no', 'exit'])
    def test1_order_w_no_funds(self, mock_input):
        expected_output = "Sorry for the inconvenience but your funds are insufficient.\n"
        with mock.patch('builtins.print') as mock_print:
            with self.assertRaises(NoFundsError):
                sim_shop()
            mock_print.assert_called_with(expected_output)

    @mock.patch('builtins.input', side_effect=['Red velvet cehesecak', 'exit'])
    def test2_order_wrong_spelling(self, mock_input):
        expected_output = "Sorry, we don't sell that cake. Please try again next time.\n"
        with mock.patch('builtins.print') as mock_print:
            sim_shop()
            mock_print.assert_called_with(expected_output)

    @mock.patch('builtins.input', side_effect=['Vegan mango cheesecake', 'yes', 3, 'Vegan mango cheesecake', 'yes', 5,
                                               'Vegan mango cheesecake', 'yes', 7])
    def test3_order_after_three_attempts_still_insufficient_funds(self, mock_input):
        expected_output = "Sorry, you reached the maximum number of attempts. You can come back another time!\n"
        with mock.patch('builtins.print') as mock_print:
            with self.assertRaises(MaxTriedError):
                sim_shop()
            mock_print.assert_called_with(expected_output)

    @mock.patch('builtins.input', side_effect=['Red velvet cheesecake', 'exit'])
    def test4_order_within_budget(self, mock_input):
        expected_output = "Here's your Red velvet cheesecake!\nThank you for choosing us! Let us know how we did 🧁\n"
        with mock.patch('builtins.print') as mock_print:
            sim_shop()
            mock_print.assert_called_with(expected_output)

    @mock.patch('builtins.input', side_effect=['Chocolate cake', 'exit'])
    def test5_order_cake_not_on_menu(self, mock_input):
        expected_output = "Sorry, we don't sell that cake. Please try again next time.\n"
        with mock.patch('builtins.print') as mock_print:
            sim_shop()
            mock_print.assert_called_with(expected_output)

if __name__ == '__main__':
    unittest.main()