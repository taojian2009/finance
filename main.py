from models import Asset, Outcome, Income

from finance_manager import FinanceManager
from data import asset_data, outcome_data, income_data

assets = [Asset(**item) for item in asset_data]
outcomes = [Outcome(**item) for item in outcome_data]

incomes = [Income(**item) for item in income_data]

FinanceManager.commit(assets + incomes + outcomes)
