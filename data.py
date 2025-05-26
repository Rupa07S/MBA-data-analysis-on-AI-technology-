import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os # Import the os module to handle file paths

# Set a style for better aesthetics (optional, but recommended)
sns.set_style("whitegrid")

# Define a folder to save your plots
output_folder = "charts"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# --- Section 4.1: Demographics of Respondents ---
print("--- Section 4.1: Demographics of Respondents ---")

# Table 4.1 Data
data_4_1 = {
    'Job Role/Position': ['Senior Management (CEO, Director, VP)',
                          'Department Head (Marketing, Sales, Operations, IT)',
                          'Mid-Level Management',
                          'Data Analyst/Scientist',
                          'Other (Please specify)'],
    'Frequency (n)': [50, 70, 40, 30, 10],
    'Percentage (%)': [25.0, 35.0, 20.0, 15.0, 5.0]
}
df_4_1 = pd.DataFrame(data_4_1)

print("\nTable 4.1: Respondent's Job Role/Position within the Retail Organization")
print(df_4_1.to_string(index=False)) # .to_string(index=False) for cleaner print
print("\n")

# Figure 4.1: Bar Chart
plt.figure(figsize=(10, 6)) # Adjust figure size as needed
sns.barplot(x='Percentage (%)', y='Job Role/Position', data=df_4_1, palette='viridis')
plt.title('Figure 4.1: Distribution of Respondent\'s Job Roles', fontsize=16)
plt.xlabel('Percentage (%)', fontsize=12)
plt.ylabel('Job Role/Position', fontsize=12)
plt.xlim(0, 40) # Set X-axis limit slightly above max percentage
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.savefig(os.path.join(output_folder, 'Figure_4_1_Job_Roles.png')) # Save the plot
plt.show() # Display the plot
plt.close() # Close the plot figure to free memory and prevent issues with too many open windows

print("Analysis and Interpretation:")
print("Table 4.1 and Figure 4.1 illustrate the distribution of respondents across various job roles within retail organizations. The highest percentage of respondents are Department Heads (35%), indicating that insights are heavily influenced by operational managers. This distribution is crucial as different job roles may have varying perspectives and experiences regarding the adoption and impact of AI and predictive analytics. For instance, senior management might focus more on overall business value and strategic alignment, while data analysts would provide insights into the technical implementation and performance metrics. The representation across different levels ensures a comprehensive understanding of the impact of AI across the organizational hierarchy.")
print("\n" + "="*80 + "\n") # Separator


# --- Section 4.2: Current Adoption and Awareness of AI and Predictive Analytics ---
print("--- Section 4.2: Current Adoption and Awareness of AI and Predictive Analytics ---")

# Table 4.2 Data
data_4_2 = {
    'AI Technology Used': ['Personalized Recommendation Engines',
                           'Chatbots/Virtual Assistants for Customer Service',
                           'AI-powered Demand Forecasting',
                           'Dynamic Pricing Algorithms',
                           'AI for Inventory Optimization',
                           'Fraud Detection Systems',
                           'AI for Supply Chain Optimization',
                           'Not currently using AI'],
    'Frequency (n)': [120, 100, 90, 70, 80, 110, 60, 20],
    'Percentage (%)': [60.0, 50.0, 45.0, 35.0, 40.0, 55.0, 30.0, 10.0]
}
df_4_2 = pd.DataFrame(data_4_2)

print("\nTable 4.2: Retail Organization's Current Use of AI Technologies")
print(df_4_2.to_string(index=False))
print("\n")

# Figure 4.2: Bar Chart
plt.figure(figsize=(12, 7))
sns.barplot(x='Percentage (%)', y='AI Technology Used', data=df_4_2, palette='coolwarm')
plt.title('Figure 4.2: Current Adoption of AI Technologies in Retail', fontsize=16)
plt.xlabel('Percentage (%)', fontsize=12)
plt.ylabel('AI Technology Used', fontsize=12)
plt.xlim(0, 70)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'Figure_4_2_AI_Adoption.png')) # Save the plot
plt.show()
plt.close()

print("Analysis and Interpretation:")
print("Table 4.2 and Figure 4.2 present the current adoption rates of various AI technologies within the surveyed retail organizations. The data reveals that Personalized Recommendation Engines are the most prevalent, adopted by 60.0% of organizations. This suggests a strong focus on enhancing customer experience and optimizing sales. AI for Supply Chain Optimization shows the lowest adoption rate (30%), indicating potential areas for future growth or specific challenges in implementation. The relatively small percentage of organizations not currently using AI (10.0%) highlights the increasing trend of digital transformation within the retail sector. This insight is critical for understanding the market readiness and potential barriers to broader AI adoption.")
print("\n" + "="*80 + "\n")


# --- Section 4.3: Perceived Impact on Business Value ---
print("--- Section 4.3: Perceived Impact on Business Value ---")

# Table 4.3 Data
data_4_3 = {
    'Aspect of Business Value': ['Increased Revenue', 'Improved Profit Margins',
                                 'Enhanced Customer Satisfaction', 'Increased Customer Loyalty/Retention',
                                 'Optimized Operational Efficiency', 'Reduced Costs',
                                 'Improved Supply Chain Management', 'Faster Time-to-Market for Products'],
    'Mean': [4.2, 4.0, 4.5, 4.3, 4.1, 3.9, 4.0, 3.7],
    'Standard Deviation': [0.6, 0.7, 0.5, 0.6, 0.7, 0.8, 0.7, 0.9]
}
df_4_3 = pd.DataFrame(data_4_3)

print("\nTable 4.3: Perceived Impact of AI/Predictive Analytics on Business Value (Likert Scale: 1=Strongly Disagree, 5=Strongly Agree)")
print(df_4_3.to_string(index=False))
print("\n")

# Figure 4.3: Bar Chart
plt.figure(figsize=(12, 7))
sns.barplot(x='Mean', y='Aspect of Business Value', data=df_4_3.sort_values(by='Mean', ascending=False), palette='magma')
plt.title('Figure 4.3: Average Perceived Impact on Business Value', fontsize=16)
plt.xlabel('Mean Score (1 = Strongly Disagree, 5 = Strongly Agree)', fontsize=12)
plt.ylabel('Aspect of Business Value', fontsize=12)
plt.xlim(0, 5) # Likert scale goes from 1 to 5
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'Figure_4_3_Business_Value_Impact.png')) # Save the plot
plt.show()
plt.close()

print("Analysis and Interpretation:")
print("Table 4.3 and Figure 4.3 illustrate the perceived impact of AI and predictive analytics on different aspects of business value, as rated by the respondents. The results show that respondents generally agree that AI/predictive analytics have a positive impact on 'Enhanced Customer Satisfaction' (Mean=4.5), indicating a strong belief in its ability to improve customer-centric outcomes. In contrast, 'Faster Time-to-Market for Products' (Mean=3.7) received a slightly lower mean score, suggesting that the impact here might be less pronounced or still developing. The relatively low standard deviations indicate a general consensus among respondents regarding these impacts. These findings are crucial for understanding the tangible and perceived benefits that retail organizations are experiencing from their AI investments.")
print("\n" + "="*80 + "\n")


# --- Section 4.4: Impact on Decision-Making Processes ---
print("--- Section 4.4: Impact on Decision-Making Processes ---")

# Table 4.4 Data
data_4_4 = {
    'Impact on Decision-Making': ['More Data-Driven Decisions', 'Faster Decision-Making',
                                  'Improved Accuracy of Decisions', 'Better Strategic Planning',
                                  'Enhanced Risk Management', 'Increased Confidence in Decisions',
                                  'Ability to Identify New Opportunities'],
    'Mean': [4.6, 4.2, 4.4, 4.3, 4.1, 4.5, 4.2],
    'Standard Deviation': [0.5, 0.7, 0.6, 0.6, 0.7, 0.5, 0.7]
}
df_4_4 = pd.DataFrame(data_4_4)

print("\nTable 4.4: Impact of AI/Predictive Analytics on Decision-Making (Likert Scale: 1=Strongly Disagree, 5=Strongly Agree)")
print(df_4_4.to_string(index=False))
print("\n")

# Figure 4.4: Bar Chart
plt.figure(figsize=(12, 7))
sns.barplot(x='Mean', y='Impact on Decision-Making', data=df_4_4.sort_values(by='Mean', ascending=False), palette='cividis')
plt.title('Figure 4.4: Average Perceived Impact on Decision-Making', fontsize=16)
plt.xlabel('Mean Score (1 = Strongly Disagree, 5 = Strongly Agree)', fontsize=12)
plt.ylabel('Impact on Decision-Making', fontsize=12)
plt.xlim(0, 5)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'Figure_4_4_Decision_Making_Impact.png')) # Save the plot
plt.show()
plt.close()

print("Analysis and Interpretation:")
print("Table 4.4 and Figure 4.4 present the respondents' views on how AI and predictive analytics have influenced decision-making processes. The consistently high mean scores, particularly for 'More Data-Driven Decisions' (Mean=4.6), demonstrate a strong perception that these technologies significantly improve the rationality and speed of decisions. This suggests a shift from traditional, intuition-based decision-making to a more evidence-based approach. The positive impact on 'Improved Accuracy of Decisions' and 'Better Strategic Planning' further reinforces the idea that AI provides valuable insights that lead to more informed and effective strategies. The relatively low standard deviations indicate a general agreement among respondents on these positive impacts, highlighting the perceived value of AI in modern retail decision-making.")
print("\n" + "="*80 + "\n")


# --- Section 4.5: Challenges in AI/Predictive Analytics Implementation ---
print("--- Section 4.5: Challenges in AI/Predictive Analytics Implementation ---")

# Table 4.5 Data
data_4_5 = {
    'Challenge': ['Lack of Skilled Personnel (Data Scientists, AI Engineers)',
                  'High Cost of Implementation and Maintenance',
                  'Data Quality and Availability Issues',
                  'Integration with Existing Systems',
                  'Resistance to Change within the Organization',
                  'Lack of Clear ROI/Business Case',
                  'Ethical Concerns (e.g., Data Privacy)',
                  'Other (Please specify)'],
    'Frequency (n)': [100, 80, 70, 60, 50, 40, 30, 10],
    'Percentage (%)': [50.0, 40.0, 35.0, 30.0, 25.0, 20.0, 15.0, 5.0]
}
df_4_5 = pd.DataFrame(data_4_5)

print("\nTable 4.5: Major Challenges in AI/Predictive Analytics Implementation")
print(df_4_5.to_string(index=False))
print("\n")

# Figure 4.5: Bar Chart
plt.figure(figsize=(12, 7))
sns.barplot(x='Percentage (%)', y='Challenge', data=df_4_5.sort_values(by='Percentage (%)', ascending=False), palette='plasma')
plt.title('Figure 4.5: Key Challenges in AI/Predictive Analytics Implementation', fontsize=16)
plt.xlabel('Percentage (%)', fontsize=12)
plt.ylabel('Challenge', fontsize=12)
plt.xlim(0, 60)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'Figure_4_5_Implementation_Challenges.png')) # Save the plot
plt.show()
plt.close()

print("Analysis and Interpretation:")
print("Table 4.5 and Figure 4.5 highlight the primary challenges retail organizations encounter during the implementation of AI and predictive analytics. The most frequently cited challenge is 'Lack of Skilled Personnel,' reported by 50.0% of respondents. This indicates a significant talent gap in the industry, which can impede the effective deployment and utilization of these advanced technologies. High Cost of Implementation and Maintenance is also a considerable hurdle, suggesting concerns about the financial feasibility or tangible returns on AI investments. Data-related issues like 'Data Quality and Availability' are also prominent, underscoring the foundational importance of robust data infrastructure for successful AI initiatives. Addressing these challenges through targeted training, strategic partnerships, and clear business case development will be crucial for accelerating AI adoption in the retail sector.")
print("\n" + "="*80 + "\n")


# --- Section 4.6: Future Investment Plans in AI/Predictive Analytics (Pie Chart) ---
print("--- Section 4.6: Future Investment Plans in AI/Predictive Analytics ---")

# Table 4.6 Data
data_4_6 = {
    'Future Plan': ['Significantly Increase Investment', 'Moderately Increase Investment',
                    'Maintain Current Investment Level', 'Decrease Investment', 'Not Sure'],
    'Frequency (n)': [90, 80, 20, 5, 5],
    'Percentage (%)': [45.0, 40.0, 10.0, 2.5, 2.5]
}
df_4_6 = pd.DataFrame(data_4_6)

print("\nTable 4.6: Future Investment Plans in AI/Predictive Analytics")
print(df_4_6.to_string(index=False))
print("\n")

# Figure 4.6: Pie Chart
plt.figure(figsize=(9, 9))
plt.pie(df_4_6['Percentage (%)'], labels=df_4_6['Future Plan'], autopct='%1.1f%%',
        startangle=90, colors=sns.color_palette('pastel'))
plt.title('Figure 4.6: Future Investment Plans in AI/Predictive Analytics', fontsize=16)
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'Figure_4_6_Future_Investment.png')) # Save the plot
plt.show()
plt.close() # Close the last plot as well

print("Analysis and Interpretation:")
print("Table 4.6 and Figure 4.6 illustrate the future investment intentions of retail organizations regarding AI and predictive analytics. A substantial majority of respondents (85.0%) plan to either 'Significantly Increase Investment' or 'Moderately Increase Investment,' indicating a strong positive outlook and growing confidence in the value proposition of these technologies. Only a small fraction anticipates decreasing investment (2.5%), suggesting that the industry recognizes the long-term strategic importance of AI. This forward-looking perspective underscores the ongoing digital transformation within retail and the increasing integration of AI into core business operations. The high commitment to future investment highlights the perceived competitive advantage and transformative potential of AI and predictive analytics in the retail landscape.")
print("\n" + "="*80 + "\n")