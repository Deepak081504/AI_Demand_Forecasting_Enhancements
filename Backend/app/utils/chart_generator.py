# app/utils/chart_generator.py
import matplotlib
matplotlib.use('Agg')  # Server-side rendering (GUI illama run aaga)
import matplotlib.pyplot as plt
import os
from datetime import datetime

def generate_forecast_chart(dates: list, actual_values: list, predicted_values: list, category: str, region: str) -> str:
    """
    Actual vs Predicted data vechu matplotlib chart generate panni image aaga save panra function.
    """
    # Create directory if it doesn't exist
    chart_dir = "uploads/reports/charts"
    os.makedirs(chart_dir, exist_ok=True)

    # Plot configuration
    plt.figure(figsize=(10, 6))
    
    # Plot Actual Values (if available)
    if actual_values and any(actual_values):
        plt.plot(dates[:len(actual_values)], actual_values, label="Actual Demand", marker='o', color='blue', linewidth=2)
    
    # Plot Predicted Values
    plt.plot(dates, predicted_values, label="AI Forecast", marker='x', linestyle='--', color='red', linewidth=2)

    # Styling the chart
    plt.title(f"Demand Forecasting: {category} - {region}", fontsize=14, fontweight='bold')
    plt.xlabel("Timeline (Dates)", fontsize=12)
    plt.ylabel("Demand Metric / Volume", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()

    # Save chart as PNG
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"chart_{category}_{region}_{timestamp}.png"
    filepath = os.path.join(chart_dir, filename)
    
    plt.savefig(filepath, dpi=300)
    plt.close() # Free up memory
    
    return filepath