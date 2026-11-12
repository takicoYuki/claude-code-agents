"""動画から一定間隔でフレーム画像を書き出す（ffmpeg使用）"""
import argparse
import subprocess
import sys
from pathlib import Path


def main():
    p = argparse.ArgumentParser()
    p.add_argument("video", help="動画ファイルのパス")
    p.add_argument("--every", type=float, default=1.0, help="何秒ごとに書き出すか")
    p.add_argument("--width", type=int, default=768, help="画像の横幅")
    a = p.parse_args()

    video = Path(a.video)
    if not video.exists():
        sys.exit(f"動画が見つかりません: {video}")

    out = video.parent / f"{video.stem}_frames"
    out.mkdir(exist_ok=True)
    fps = 1.0 / a.every

    cmd = [
        "ffmpeg", "-y", "-loglevel", "error", "-i", str(video),
        "-vf", f"fps={fps},scale={a.width}:-1",
        str(out / "f%04d.jpg"),
    ]
    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        sys.exit("ffmpegが見つかりません。インストールしてPATHを通してください。")

    # 連番を秒数の名前に付け替える（t0003.jpg = 3秒目）
    for i, f in enumerate(sorted(out.glob("f*.jpg"))):
        sec = i * a.every
        f.rename(out / f"t{sec:06.1f}.jpg".replace(".0.jpg", ".jpg"))

    print(f"書き出し完了: {out}  ({len(list(out.glob('*.jpg')))}枚)")


if __name__ == "__main__":
    main()
