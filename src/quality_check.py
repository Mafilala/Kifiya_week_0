def checkMissingData(df, col):
    return df[col].isnull().sum(0)


def getNumberOfNegativeValue(df, col):
    return df[col].apply(lambda x: x < 0).sum(0)


def getPercentageOfNegativeValue(df, col):
    total_rows = df.shape[0]
    negative_count = getNumberOfNegativeValue(df, col)
    return (negative_count / total_rows) * 100