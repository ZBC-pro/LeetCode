import os
import requests

# 定义文件列表
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
base_directories = ["original_files", "txt_files"]
sub_directories = ["entities", "relations", "prerequisites"]

# 创建基础目录结构
for base_dir in base_directories:
    for sub_dir in sub_directories:
        os.makedirs(os.path.join(base_dir, sub_dir), exist_ok=True)

# 下载文件
def download_file(url, original_path, txt_path, max_size_mb):
    """下载文件并限制最大文件大小，同时保存为 .txt"""
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        # 获取内容大小
        total_size_mb = int(response.headers.get("Content-Length", 0)) / (1024 * 1024)
        if total_size_mb > max_size_mb:
            print(f"Skipping {url}: file size {total_size_mb:.2f} MB exceeds {max_size_mb} MB")
            return False

        # 保存原始文件
        os.makedirs(os.path.dirname(original_path), exist_ok=True)
        with open(original_path, "wb") as original_file:
            for chunk in response.iter_content(chunk_size=8192):
                original_file.write(chunk)

        print(f"Saved original: {original_path}")

        # 保存为文本文件
        with open(original_path, "r", encoding="utf-8") as original_file:
            content = original_file.read()

        os.makedirs(os.path.dirname(txt_path), exist_ok=True)
        with open(txt_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(content)

        print(f"Saved as TXT: {txt_path}")
        return True

    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return False
    except Exception as e:
        print(f"Error processing file {original_path}: {e}")
        return False

# 主逻辑
failed_files = []  # 记录失败的文件
for file_path in files:
    url = f"{base_url}{file_path}"

    # 根据文件路径分类
    category = file_path.split("/")[0]  # 提取文件夹名称（entities、relations、prerequisites）
    original_path = os.path.join("original_files", category, os.path.basename(file_path))
    txt_path = os.path.join("txt_files", category, os.path.basename(file_path) + ".txt")

    print(f"Downloading {file_path} ...")
    success = download_file(url, original_path, txt_path, max_size_mb=50)  # 最大文件大小限制为 50MB
    if not success:
        failed_files.append(file_path)

# 打印失败的文件
if failed_files:
    print("\nThe following files failed to download:")
    for failed in failed_files:
        print(failed)
else:
    print("\nAll files downloaded successfully!")