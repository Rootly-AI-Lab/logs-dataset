import pandas as pd


def create_csv():
    LOGS_FILEPATH = "apache/apache_error.log"
    LABELS_FILEPATH = "apache/apache_error_parsed.csv"
    OUTPUT_FILEPATH = "apache/apache_error_compiled.csv"

    logs_list = []
    with open(LOGS_FILEPATH, "r") as logs_fp:
        logs_list = logs_fp.readlines()

    if len(logs_list) < 1:
        raise IndexError(f"logs_list from {LOGS_FILEPATH} has no lines")

    labels_df = pd.read_csv(LABELS_FILEPATH)
    print(labels_df.head())

    print(len(logs_list))
    print(labels_df.shape)

    if len(logs_list) != labels_df.shape[0]:
        raise IndexError(
            "length of logs_list does not match length of labels_df.shape[0]"
        )

    target_df = pd.DataFrame(columns=["Log", "LogLevel"])

    N = 100 # TODO: add option for mini (100) or full dataset

    for i in range(N):
        target_df.loc[i] = [logs_list[i], labels_df["LogLevel"].values[i]]


    target_df.to_csv(OUTPUT_FILEPATH, index=False)

    print(labels_df["LogLevel"].values)


if __name__ == "__main__":
    create_csv()
