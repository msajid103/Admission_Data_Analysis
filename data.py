import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
adm_df=pd.read_csv('adm_data.csv')
sns.set_palette("hls")

# -------------------------------- GRE Score ----------------------------

GRE_score_range = (adm_df['GRE Score'].max()-adm_df['GRE Score'].min())/7
GRE_interval = [290,297,304,311,318,325,332,340]
sns.histplot(x="GRE Score", data=adm_df, bins = GRE_interval)
plt.show()

# ------------------X------------- GRE Score ------------X---------------

# -------------------------------- TOEFL Score ----------------------------


TOEFL_Score_range = (adm_df['TOEFL Score'].max()-adm_df['TOEFL Score'].min())/7
TOEFL_interval = [92,96,100,104,108,112,116,120]
sns.histplot( x="TOEFL Score", data=adm_df, color='#0000FF', bins=TOEFL_interval)
plt.show()


# ---------X--------- TOEFL Score ---------X------------

# ------------------ SOP ------------------------

sns.countplot(x='SOP',data=adm_df)
plt.show()

# -----------X----------- SOP -------------X--------------

# ----------------------- LOR ---------------------------

sns.countplot(x='LOR ',data=adm_df)
plt.show()

# -----------X---------- LOR -------------X--------------


# -------------------- Chance of Admit vs GRE score -----------------

sns.lmplot(x='GRE Score',y='Chance of Admit ',data=adm_df,hue='Research')
plt.title('Chance of Admit vs GRE score')
plt.show()

# ------------X-------- Chance of Admit vs GRE score ---------X---------

# -------------------- Chance of Admit vs TOEFL score -----------------

sns.lmplot(x='TOEFL Score',y='Chance of Admit ',data=adm_df,hue='Research')
plt.title('Chance of Admit vs TOEFL score')
plt.show()

# -------------X------- Chance of Admit vs TOEFL score ---------X--------

# -------------------- Chance of Admit vs CGPA  -----------------

sns.lmplot(x='CGPA',y='Chance of Admit ',data=adm_df,hue='Research')
plt.title('Chance of Admit vs CGPA')
plt.show()

# -----------X--------- Chance of Admit vs CGPA  ---------X--------
