import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style for better visualizations
plt.style.use('seaborn')
sns.set_palette("husl")

# Read the CSV file
csv_file = os.path.join('data', 'annual-enterprise-survey-2023-financial-year-provisional.csv')
df = pd.read_csv(csv_file)

# Convert Value column to numeric, removing any currency symbols and commas
df['Value'] = pd.to_numeric(df['Value'].str.replace(',', ''), errors='coerce')

def analyze_industry_trends():
    """Analyze and visualize trends by industry over time"""
    # Get total value by industry and year for Level 1 industries
    industry_trends = df[df['Industry_aggregation_NZSIOC'] == 'Level 1'].pivot_table(
        values='Value',
        index='Year',
        columns='Industry_name_NZSIOC',
        aggfunc='sum'
    )
    
    # Plot the trends
    plt.figure(figsize=(15, 8))
    industry_trends.plot(marker='o')
    plt.title('Industry Trends Over Time')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('industry_trends.png')
    plt.close()

def analyze_variable_distribution():
    """Analyze the distribution of different financial variables"""
    # Get average values by variable name
    var_dist = df.groupby('Variable_name')['Value'].mean().sort_values(ascending=False)
    
    # Plot top 15 variables
    plt.figure(figsize=(12, 6))
    var_dist.head(15).plot(kind='bar')
    plt.title('Average Values by Financial Variable (Top 15)')
    plt.xlabel('Variable Name')
    plt.ylabel('Average Value')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('variable_distribution.png')
    print("Variable distribution analysis completed")
    plt.close()

def analyze_industry_composition():
    """Analyze the composition of industries in the most recent year"""
    # Get the most recent year's data
    latest_year = df['Year'].max()
    latest_data = df[df['Year'] == latest_year]
    
    # Calculate total value by industry
    industry_totals = latest_data.groupby('Industry_name_NZSIOC')['Value'].sum().sort_values(ascending=True)
    
    # Plot horizontal bar chart
    plt.figure(figsize=(12, 8))
    industry_totals.plot(kind='barh')
    plt.title(f'Industry Composition ({latest_year})')
    plt.xlabel('Total Value')
    plt.ylabel('Industry')
    plt.tight_layout()
    plt.savefig('industry_composition.png')
    plt.close()

def calculate_growth_rates():
    """Calculate and display year-over-year growth rates"""
    # Calculate year-over-year growth rates for each industry
    industry_data = df[df['Industry_aggregation_NZSIOC'] == 'Level 1'].pivot_table(
        values='Value',
        index='Year',
        columns='Industry_name_NZSIOC',
        aggfunc='sum'
    )
    
    growth_rates = industry_data.pct_change() * 100
    
    # Calculate average growth rate for each industry
    avg_growth = growth_rates.mean().sort_values(ascending=False)
    
    # Plot average growth rates
    plt.figure(figsize=(12, 6))
    avg_growth.plot(kind='bar')
    plt.title('Average Year-over-Year Growth Rate by Industry')
    plt.xlabel('Industry')
    plt.ylabel('Average Growth Rate (%)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('growth_rates.png')
    plt.close()
    
    return avg_growth

def main():
    print("Starting analysis...")
    
    # Run all analyses
    analyze_industry_trends()
    print("✓ Industry trends analysis completed")
    
    analyze_variable_distribution()
    print("✓ Variable distribution analysis completed")
    
    analyze_industry_composition()
    print("✓ Industry composition analysis completed")
    
    growth_rates = calculate_growth_rates()
    print("\nAverage Growth Rates by Industry:")
    print(growth_rates)
    print("\n✓ Growth rate analysis completed")
    
    print("\nAll analyses completed! Check the generated PNG files for visualizations.")

if __name__ == "__main__":
    main() 