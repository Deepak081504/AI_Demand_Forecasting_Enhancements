# app/reports/analytics_summary.py
def build_analytics_summary_dictionary(records: list):
    return {
        "summary_count": len(records),
        "mean_predicted_metric": sum([r.predicted_value for r in records]) / len(records) if records else 0
    }