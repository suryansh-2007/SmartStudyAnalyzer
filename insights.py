import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('default')
print(" Creating Professional Graphs...")

def generate_insights():
    df = pd.read_csv('student_data.csv')
    
    # KEY INSIGHTS
    print(" SMART INSIGHTS:")
    print(f"• Average Study Hours: {df['Study_Hours'].mean():.1f}")
    print(f"• Average Final Marks: {df['Final_Marks'].mean():.1f}%")
    print(f"• Best Subject: {df.groupby('Subject')['Final_Marks'].mean().idxmax()}")
    print(f"• Low study (<2hrs) avg: {df[df['Study_Hours']<2]['Final_Marks'].mean():.1f}%")
    
    # 3 PROFESSIONAL GRAPHS
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    # Graph 1: Study vs Marks
    axes[0].scatter(df['Study_Hours'], df['Final_Marks'], alpha=0.6, color='skyblue')
    axes[0].set_title('Study Hours vs Marks')
    axes[0].set_xlabel('Study Hours'); axes[0].set_ylabel('Marks')
    
    # Graph 2: Subject Performance
    subj_avg = df.groupby('Subject')['Final_Marks'].mean()
    axes[1].bar(subj_avg.index, subj_avg.values, color=['red','blue','green'])
    axes[1].set_title('Subject Performance')
    axes[1].tick_params(axis='x', rotation=45)
    
    # Graph 3: Marks Distribution
    axes[2].hist(df['Final_Marks'], bins=20, color='purple', alpha=0.7)
    axes[2].set_title('Marks Distribution')
    axes[2].set_xlabel('Final Marks')
    
    plt.tight_layout()
    plt.savefig('insights.png', dpi=300, bbox_inches='tight')
    plt.show()
    print(" Graphs saved: insights.png")

if __name__ == "__main__":
    generate_insights()