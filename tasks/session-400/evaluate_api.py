"""
HuggingFace 情感分析模型评估 - Inference API 在线调用版
"""

import os
import pandas as pd
import requests
import time

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

CANDIDATE_MODELS = [
    "distilbert-base-uncased-finetuned-sst-2-english",
    "siebert/sentiment-roberta-large-english",
    "textattack/roberta-base-SST-2",
    "aychang/roberta-base-imdb",
    "cardiffnlp/twitter-roberta-base-sentiment-latest",
    "nlptown/bert-base-multilingual-uncased-sentiment",
    "finiteautomata/bertweet-base-sentiment-analysis",
    "mrm8488/deberta-v3-finetuned-sst2",
    "microsoft/xtremedistil-l12-h384-sst-2-english",
    "lxyuan/distilbert-base-multilingual-cased-sentiments-student",
]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(SCRIPT_DIR, "datasets", "imdb_top_500.csv")
SUBSET_SIZE = 50
API_URL = "https://hf-mirror.com/api/models"


def hf_to_label(pred):
    label = pred["label"].upper()
    if label in ("POSITIVE", "POS", "LABEL_1"):
        return 1
    if label in ("NEGATIVE", "NEG", "LABEL_0"):
        return 0
    if "star" in label.lower():
        stars = int(label.split()[0])
        return 1 if stars >= 4 else 0
    if label == "NEUTRAL":
        return 0
    return 0


def query_model(model_name, text):
    """通过 Inference API 调用模型"""
    api = f"https://hf-mirror.com/models/{model_name}/pipeline/sentiment-analysis"
    try:
        resp = requests.post(api, json={"inputs": text}, timeout=30)
        if resp.status_code == 200:
            result = resp.json()
            if isinstance(result, list) and len(result) > 0:
                if isinstance(result[0], list):
                    return result[0][0]
                return result[0]
        return None
    except Exception as e:
        return None


def evaluate_model_api(model_name, reviews, true_labels):
    print(f"\n{'='*60}")
    print(f"模型: {model_name}")
    print(f"{'='*60}")

    # 先测一条看标签格式
    test = query_model(model_name, "This movie is great")
    if test is None:
        print("API 调用失败，跳过")
        return None
    print(f"测试预测: {test}")

    pred_labels = []
    correct_count = 0

    for i, review in enumerate(reviews):
        result = query_model(model_name, review)
        if result is None:
            pred_labels.append(-1)
            continue
        pred = hf_to_label(result)
        pred_labels.append(pred)
        if pred == true_labels[i]:
            correct_count += 1

        if (i + 1) % 10 == 0:
            print(f"  进度: {i+1}/{len(reviews)}")
        time.sleep(0.3)  # 避免限流

    valid = [p for p in pred_labels if p != -1]
    accuracy = correct_count / len(true_labels) if true_labels else 0

    print(f"准确率: {accuracy:.2%} ({correct_count}/{len(true_labels)})")

    for i in range(min(5, len(reviews))):
        if pred_labels[i] == -1:
            continue
        match = "✓" if pred_labels[i] == true_labels[i] else "✗"
        print(f"  {match} 真实={true_labels[i]} 预测={pred_labels[i]} | {reviews[i][:80]}...")

    return accuracy


def main():
    df = pd.read_csv(DATASET_PATH)
    reviews = df["text"].iloc[:SUBSET_SIZE].tolist()
    true_labels = df["label"].iloc[:SUBSET_SIZE].tolist()

    print(f"数据集: {DATASET_PATH}")
    print(f"评估样本数: {SUBSET_SIZE}")
    print(f"模式: HuggingFace Inference API 在线调用")

    results = {}
    for model_name in CANDIDATE_MODELS:
        acc = evaluate_model_api(model_name, reviews, true_labels)
        if acc is not None:
            results[model_name] = acc

    print(f"\n{'='*60}")
    print("汇总结果（按准确率降序）")
    print(f"{'='*60}")

    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    for model_name, accuracy in sorted_results:
        mark = " ✓ (>95%)" if accuracy > 0.95 else ""
        print(f"  {accuracy:.2%}  {model_name}{mark}")

    results_path = os.path.join(SCRIPT_DIR, "results.txt")
    with open(results_path, "w") as f:
        f.write("模型评估结果（Inference API）\n")
        f.write(f"数据集: {DATASET_PATH}\n")
        f.write(f"评估样本数: {SUBSET_SIZE}\n\n")
        for model_name, accuracy in sorted_results:
            mark = " (>95%)" if accuracy > 0.95 else ""
            f.write(f"{accuracy:.2%}  {model_name}{mark}\n")
    print(f"\n结果已保存到 {results_path}")


if __name__ == "__main__":
    main()
