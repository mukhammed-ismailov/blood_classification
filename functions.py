from  config import *

#Функция отображения гистограммы и распределения
def graph(df, col, hist_xLbl, box_Lbl):
    sns.set(style="ticks")

    fig, [ax1, ax2] = plt.subplots(ncols=2, figsize=(12, 6))

    ax1.hist(df[col])
    ax1.set_xlabel(hist_xLbl)
    ax1.set_ylabel('Количество')
    ax1.title.set_text('Гистограмма расперделения ' + col)

    sns.boxplot(data=df[col], ax=ax2)

    # ax2.boxplot(df[col])
    ax2.set_xlabel(box_Lbl)
    ax2.title.set_text('Диаграмма размаха ' + col)

    plt.show()
    print(df[col].describe())
    print(f'Число пропусков {df[col].isnull().sum()}')


def remove_outliers(df, col,val):
    index = df[df[col]>val].index
    print(f'number of rows over {val} equal {len(index)}')
    return df.drop(index)

def print_results(target ,pred, label_encoder):

    print("Overall Accuracy:", accuracy_score(target, pred))
    print("Overall Precision:", precision_score(target, pred, average='macro'))
    print("Overall Recall:", recall_score(target, pred, average='macro'))


    plt.figure(figsize=(8, 8))
    cm = confusion_matrix(target, pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues_r')
    plt.ylabel('True label')
    plt.xlabel('Predicted');
    plt.gca().yaxis.set_ticklabels(label_encoder.inverse_transform(range(0, 8)));
    plt.gca().xaxis.set_ticklabels(label_encoder.inverse_transform(range(0, 8)));
    plt.show()

