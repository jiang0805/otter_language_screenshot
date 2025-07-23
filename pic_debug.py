import os
import hashlib

def get_file_md5(file_path, chunk_size=8192):
    md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()

def deduplicate_images(folder):
    seen_hashes = set()
    for root, dirs, files in os.walk(folder):
        for fn in files:
            if fn.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.tiff')):
                abs_path = os.path.join(root, fn)
                file_hash = get_file_md5(abs_path)
                if file_hash in seen_hashes:
                    print(f'Deleting duplicate: {abs_path}')
                    os.remove(abs_path)
                else:
                    seen_hashes.add(file_hash)

if __name__ == '__main__':
    img_folder = r'/Users/jiangwenqiu/otter_try/language_test/TestReport_History/Report_20250723122834/QA的iPhone/temp'  # 如 r'D:\Test\Images'
    deduplicate_images(img_folder)
    print("去重完成。")
