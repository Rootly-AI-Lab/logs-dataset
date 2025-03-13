import tqdm


def run() -> dict:
    return {"data": []}


def run_eval(model_func, model=None, verbose=False):
    FILEPATH_ERRORLOG = "apache/apache_error.log"
    FILEPATH_ERRORLOG_GT = "apache/apache_error_parsed.csv"
    with open(FILEPATH_ERRORLOG, "r") as fp_errorlog:
        error_log_lines = fp_errorlog.readlines()
    with open(FILEPATH_ERRORLOG_GT) as fp_errorlog_gt:
        error_log_lines_gt = fp_errorlog_gt.readlines()

    correct_count = 0
    total_count = 100

    for i in tqdm.trange(1, total_count):
        if verbose:
            print(error_log_lines[i])
            print(error_log_lines_gt[i].split(",")[-1])
        y_true = error_log_lines_gt[i].split(",")[-1]
        pred = model_func(error_log_lines[i], model=model)
        if verbose:
            print(y_true)
        if len(pred.strip()) == 2:
            if pred.strip() == y_true.strip():
                correct_count += 1
        elif len(pred.strip()) > 2:
            if y_true.strip() in pred.strip()[:3]:
                correct_count += 1
        if verbose:
            print()

    acc = correct_count / total_count

    return {"results": {"acc": acc}}
