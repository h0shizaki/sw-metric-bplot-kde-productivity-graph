import pandas as pd
from util import filter_dataset, load_data
import matplotlib.pyplot as plt


if __name__ == '__main__':
    path ='./resource/desharnais.csv'
    to_drop = ['id', 'Project', 'TeamExp', 'ManagerExp', 'YearEnd', 'Length', 'Transactions', 'Entities', 'PointsNonAdjust', 'Adjustment']
    dataset = load_data(path,to_drop)

    group_a, group_b , group_c = filter_dataset(dataset)
    prod_a = group_a['Productivity']
    prod_b = group_b['Productivity']
    prod_c = group_c['Productivity']

    # # create kde
    s1,s2,s3 = pd.Series(prod_a), pd.Series(prod_b), pd.Series(prod_c)
    s1.plot.kde(alpha=0.4, lw=4, grid=True)
    s2.plot.kde(alpha=0.4, lw=4, grid=True).set_xlabel("Productivity")
    figure = s3.plot.kde(alpha=0.4, lw=4, grid=True, title="KDE of productivity").get_figure()
    figure.legend(['Language 1', 'Language 2', 'Language 3'], fontsize=8)
    figure.savefig('KDE.png')

    # # create boxplot
    fig,ax = plt.subplots()
    ax.boxplot([s1,s2,s3])
    ax.set_title("Productivity BoxPlot")
    fig.savefig("BPlot.png", format="png")