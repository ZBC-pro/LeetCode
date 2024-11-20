import os
import requests

# 文件列表
files = [
    "entities/reply.json",
    "entities/video.json",
    "entities/comment.json",
    "entities/course.json",
    "entities/other.json",
    "entities/paper.json",
    "entities/problem.json",
    "entities/school.json",
    "entities/teacher.json",
    "entities/user.json",
    "entities/concept.json",
    "relations/course-school.txt",
    "relations/course-teacher.txt",
    "relations/user-comment.txt",
    "relations/video_id-ccid.txt",
    "relations/comment-reply.txt",
    "relations/concept-other.txt",
    "relations/course-comment.txt",
    "relations/concept-video.txt",
    "relations/exercise-problem.txt",
    "relations/user-reply.txt",
    "relations/concept-comment.txt",
    "relations/concept-paper.txt",
    "relations/concept-problem.txt",
    "relations/concept-reply.json",
    "relations/course-field.json",
    "relations/reply-reply.txt",
    "relations/user-problem.json",
    "relations/user-video.json",
    "relations/user-xiaomu.json",
    "prerequisites/psy.json",
    "prerequisites/cs.json",
    "prerequisites/math.json",
]

base_url = "https://lfs.aminer.cn/misc/moocdata/data/mooccube2/"

# 确保目录存在
directories = ["original_files", "txt_files"]
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# 下载文件
def download_file(url, original_path, txt_path, max_download_mb, timeout=300):
    """下载文件限制为前 max_download_mb MB"""
    try:
        response = requests.get(url, stream=True, timeout=timeout)
        response.raise_for_status()

        # 流式下载文件的前 max_download_mb MB
        downloaded_size = 0
        max_download_bytes = max_download_mb * 1024 * 1024
        os.makedirs(os.path.dirname(original_path), exist_ok=True)

        with open(original_path, "wb") as original_file:
            for chunk in response.iter_content(chunk_size=8192):
                if downloaded_size + len(chunk) > max_download_bytes:
                    # 剩余部分不够一个 chunk 的情况
                    original_file.write(chunk[:max_download_bytes - downloaded_size])
                    break
                original_file.write(chunk)
                downloaded_size += len(chunk)

        print(f"Saved first {max_download_mb} MB: {original_path}")

        # 保存为文本文件
        os.makedirs(os.path.dirname(txt_path), exist_ok=True)
        with open(txt_path, "w", encoding="utf-8") as txt_file:
            with open(original_path, "r", encoding="utf-8") as original_file:
                txt_file.write(original_file.read())

        print(f"Saved as TXT: {txt_path}")
        return True

    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return False
    except Exception as e:
        print(f"Error processing file {original_path}: {e}")
        return False

# 主逻辑
failed_files = []
for file_path in files:
    url = f"{base_url}{file_path}"
    category = file_path.split("/")[0]
    original_path = os.path.join("original_files", category, os.path.basename(file_path))
    txt_path = os.path.join("txt_files", category, os.path.basename(file_path) + ".txt")

    print(f"Downloading {file_path} ...")
    success = download_file(url, original_path, txt_path, max_download_mb=10, timeout=300)
    if not success:
        failed_files.append(file_path)

# 打印结果
if failed_files:
    print("\nThe following files failed to download:")
    for failed in failed_files:
        print(failed)
else:
    print("\nAll files downloaded successfully!")