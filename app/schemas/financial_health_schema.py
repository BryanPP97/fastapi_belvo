from pydantic import BaseModel

class FinancialHealthSummary(BaseModel):
    total_inflow: float
    total_outflow: float
    financial_health_score: float  # ratio de ingresos a egresos

