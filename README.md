# NBA Player Stats Analysis (2024–2025)
This is a Python project analyzing NBA player stats for the 2024–2025 season. It includes basic data exploration and visualizations.

**Files**
- NBA Player Stats 24-25.py – Main Python script for analysis
- nbaplayerstats2425.csv – Dataset of player statistics
- 3PA vs Total Points (2024-2025 NBA Season).png – Scatter plot of 3-point attempts vs total points
- Average Team FG% (2024-2025 NBA Season).png – Bar chart of team field-goal percentages
- Distribution of FG% (2024-2025 NBA Season).png – Histogram of field-goal percentages

**About**

This project explores player and team performance in the 2024–2025 NBA season. The analysis answers questions like:
- How do three-point attempts relate to total points scored?
- Which teams have the highest average field-goal percentages?
- How are field-goal percentages distributed across players?

**Program Output**
```text
Top 10 FG% Scorers:
        Player Team  PTS   FG%  3PA   3P%
  Jaxson Hayes  LAL  383 0.722    3 0.000
 Jarrett Allen  CLE 1103 0.706    5 0.000
     Adem Bona  PHI  337 0.703    1 0.000
   Luke Kornet  BOS  441 0.668    3 0.000
Walker Kessler  UTA  641 0.663   34 0.176
 Neemias Queta  BOS  310 0.650    3 0.000
  Jakob Poeltl  TOR  824 0.627    3 0.333
Brandon Clarke  MEM  534 0.621   17 0.059
 Mason Plumlee  PHO  333 0.619    4 0.000
  Goga Bitadze  ORL  502 0.611   28 0.107

Average Team FG%:
Team
DEN    0.502875
MEM    0.499818
PHO    0.495333
BOS    0.494700
IND    0.486273
CLE    0.486167
LAL    0.484727
OKC    0.484000
ATL    0.478727
NYK    0.478000
MIL    0.477700
SAC    0.472444
GSW    0.471167
PHI    0.470636
MIA    0.470000
SAS    0.466200
UTA    0.463182
CHI    0.463167
NOP    0.462917
LAC    0.462444
POR    0.461500
ORL    0.460909
DET    0.459364
TOR    0.458000
HOU    0.454333
DAL    0.448333
MIN    0.447286
CHO    0.445818
WAS    0.443455
BRK    0.437250

Top 10 3PT Shooters (Min 150 Attempts):
         Player Team  3PA   3P%  PTS
     Seth Curry  CHO  182 0.456  444
    Zach LaVine  2TM  536 0.446 1724
      Ty Jerome  CLE  253 0.439  878
 Taurean Prince  MIL  335 0.439  656
     Vit Krejci  ATL  206 0.437  412
   Aaron Gordon  DEN  172 0.436  748
   Luke Kennard  MEM  261 0.433  576
  Nicolas Batum  LAC  203 0.433  313
     Keon Ellis  SAC  321 0.433  666
Harrison Barnes  SAS  360 0.433 1011
```
**Key Findings**
- **3PA vs Total Points:** More 3-point attempts generally lead to higher total points, but some high scorers rely on 2-point shots.  
- **Top Teams by FG%:** Denver Nuggets and Memphis Grizzlies had the highest average field-goal percentages, while Washington Wizards and Brooklyn Nets had the lowest average field-goal percentages.
- **FG% Distribution:** Most players cluster around 40–50% FG%, with a few outliers. 

**Data Source**

The dataset used in this project was obtained from basketball-reference.com for the 2024–2025 NBA season.
- https://www.basketball-reference.com/leagues/NBA_2025_totals.html
