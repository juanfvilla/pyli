#https://www.datacamp.com/tutorial/how-to-make-gantt-chart-in-python-matplotlib?utm_source=customerio&utm_medium=email&utm_campaign=221122_1-newsletter-reg_2-b2c_3-all_4-na_5-na_6-dc-insights_7-na_8-emal-ci_9-na_10-bau_11-email&utm_content=blast&utm_term=blog
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime as dt
#---------------
df = pd.DataFrame({'task': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
                  'team': ['R&D', 'Accounting', 'Sales', 'Sales', 'IT', 'R&D', 'IT', 'Sales', 'Accounting', 'Accounting', 'Sales', 'IT'],
                  'start': pd.to_datetime(['20 Oct 2022', '24 Oct 2022', '26 Oct 2022', '31 Oct 2022', '3 Nov 2022', '7 Nov 2022', '10 Nov 2022', '14 Nov 2022', '18 Nov 2022', '23 Nov 2022', '28 Nov 2022', '30 Nov 2022']),
                  'end': pd.to_datetime(['31 Oct 2022', '28 Oct 2022', '31 Oct 2022', '8 Nov 2022', '9 Nov 2022', '18 Nov 2022', '17 Nov 2022', '22 Nov 2022', '23 Nov 2022', '1 Dec 2022', '5 Dec 2022', '5 Dec 2022']),
                  'completion_frac': [1, 1, 1, 1, 1, 0.95, 0.7, 0.35, 0.1, 0, 0, 0]})
#---------------
print(df)
#---------------
df['days_to_start'] = (df['start'] - df['start'].min()).dt.days
#---------------
df['days_to_end'] = (df['end'] - df['start'].min()).dt.days
#---------------
df['task_duration'] = df['days_to_end'] - df['days_to_start'] + 1  # to include also the end date
#---------------
df['completion_days'] = df['completion_frac'] * df['task_duration']
#---------------
print(df)
#---------------
plt.barh(y=df['task'], width=df['task_duration'], left=df['days_to_start'])
plt.show()
#---------------
# 1
df2 = df[df['team']=='Sales'][['task', 'team', 'start', 'end']]

# 2
df2.rename(columns={'start': 'start_1', 'end': 'end_1'}, inplace=True)
df2.reset_index(drop=True, inplace=True)

# 3
df2['start_2'] = pd.to_datetime([None, '10 Nov 2022', '25 Nov 2022', None])
df2['end_2'] = pd.to_datetime([None, '14 Nov 2022', '28 Nov 2022', None])
df2['start_3'] = pd.to_datetime([None, None, '1 Dec 2022', None])
df2['end_3'] = pd.to_datetime([None, None, '5 Dec 2022', None])

# 4
for i in [1, 2, 3]:
    suffix = '_' + str(i)
    df2['days_to_start' + suffix] = (df2['start' + suffix] - df2['start_1'].min()).dt.days
    df2['days_to_end' + suffix] = (df2['end' + suffix] - df2['start_1'].min()).dt.days
    df2['task_duration' + suffix] = df2['days_to_end' + suffix] - df2['days_to_start' + suffix] + 1


print(df2)
#---------------
# 1
fig, ax = plt.subplots()

# 2
for index, row in df2.iterrows():
    if row['start_2'] is None:
        ax.barh(y=df2['task'], width=df2['task_duration_1'], left=df2['days_to_start_1'])
    elif row['start_2'] is not None and row['start_3'] is None:
        ax.broken_barh(xranges=[(row['days_to_start_1'], row['task_duration_1']), (row['days_to_start_2'], row['task_duration_2'])], yrange=(index + 1, 0.5))
    else:
        ax.broken_barh(xranges=[(row['days_to_start_1'], row['task_duration_1']), (row['days_to_start_2'], row['task_duration_2']), (row['days_to_start_3'], row['task_duration_3'])], yrange=(index + 1, 0.5))

# 3
ax.set_yticks([1.25, 2.25, 3.25, 4.25])
ax.set_yticklabels(df2['task'])

plt.show()
#---------------
ax.barh(y=df2['task'], width=df2['task_duration_1'], left=df2['days_to_start_1'])
#---------------
ax.broken_barh(xranges=[(row['days_to_start_1'], row['task_duration_1'])], yrange=(index + 1, 0.5))
#---------------
print(df)
#---------------
plt.barh(y=df['task'], width=df['task_duration'], left=df['days_to_start'])
plt.show()
#---------------
plt.barh(y=df['task'], width=df['task_duration'], left=df['days_to_start'])
plt.title('Project Management Schedule of Project X', fontsize=15)
plt.show()
#---------------
# 1
fig, ax = plt.subplots()

plt.barh(y=df['task'], width=df['task_duration'], left=df['days_to_start'] + 1)
plt.title('Project Management Schedule of Project X', fontsize=15)

# 2
plt.gca().invert_yaxis()

# 3
xticks = np.arange(5, df['days_to_end'].max() + 2, 7)

# 4
xticklabels = pd.date_range(start=df['start'].min() + dt.timedelta(days=4), end=df['end'].max()).strftime("%d/%m")
# 5
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels[::7])

# 6
ax.xaxis.grid(True, alpha=0.5)

plt.show()
#---------------
# 1
team_colors = {'R&D': 'c', 'Accounting': 'm', 'Sales': 'y', 'IT': 'b'}

# 2
fig, ax = plt.subplots()

# 3
for index, row in df.iterrows():
    plt.barh(y=row['task'], width=row['task_duration'], left=row['days_to_start'] + 1, color=team_colors[row['team']])

# 4
plt.title('Project Management Schedule of Project X', fontsize=15)
plt.gca().invert_yaxis()
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels[::7])
ax.xaxis.grid(True, alpha=0.5)
plt.show()
#---------------
patches = []
for team in team_colors:
    patches.append(matplotlib.patches.Patch(color=team_colors[team]))
#---------------
fig, ax = plt.subplots()
for index, row in df.iterrows():
    plt.barh(y=row['task'], width=row['task_duration'], left=row['days_to_start'] + 1, color=team_colors[row['team']])
plt.title('Project Management Schedule of Project X', fontsize=15)
plt.gca().invert_yaxis()
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels[::7])
ax.xaxis.grid(True, alpha=0.5)

# Adding a legend
ax.legend(handles=patches, labels=team_colors.keys(), fontsize=11)

plt.show()
#---------------
fig, ax = plt.subplots()

for index, row in df.iterrows():

    # Adding a lower bar - for the overall task duration
    plt.barh(y=row['task'], width=row['task_duration'], left=row['days_to_start'] + 1, color=team_colors[row['team']], alpha=0.4)

    # Adding an upper bar - for the status of completion
    plt.barh(y=row['task'], width=row['completion_days'], left=row['days_to_start'] + 1, color=team_colors[row['team']])

plt.title('Project Management Schedule of Project X', fontsize=15)
plt.gca().invert_yaxis()
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels[::7])
ax.xaxis.grid(True, alpha=0.5)
ax.legend(handles=patches, labels=team_colors.keys(), fontsize=11)
plt.show()
#---------------
fig, ax = plt.subplots()
for index, row in df.iterrows():
    plt.barh(y=row['task'], width=row['task_duration'], left=row['days_to_start'] + 1, color=team_colors[row['team']], alpha=0.4)
    plt.barh(y=row['task'], width=row['completion_days'], left=row['days_to_start'] + 1, color=team_colors[row['team']])

plt.title('Project Management Schedule of Project X', fontsize=15)
plt.gca().invert_yaxis()
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels[::7])
ax.xaxis.grid(True, alpha=0.5)
ax.legend(handles=patches, labels=team_colors.keys(), fontsize=11)

# Marking the current date on the chart
ax.axvline(x=29, color='r', linestyle='dashed')
ax.text(x=29.5, y=11.5, s='17/11', color='r')

plt.show()
