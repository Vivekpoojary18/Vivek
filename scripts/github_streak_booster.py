#!/usr/bin/env python3
"""
GitHub Streak Booster & Daily Contribution Keeper
==================================================
Author: Vivek J Poojary
Description: CLI script to verify local repository streak status, log contributions,
             and generate clean structured commits to maintain a green GitHub graph.
"""

import os
import sys
import subprocess
import datetime
import argparse

def get_git_output(cmd, cwd=None):
    env = os.environ.copy()
    env["GIT_CONFIG_GLOBAL"] = "/dev/null"
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd, env=env)
    return res.stdout.strip()

def check_today_contributions(repo_dir):
    today_str = datetime.date.today().isoformat()
    cmd = f'git log --author="Vivek" --since="midnight" --oneline'
    output = get_git_output(cmd, cwd=repo_dir)
    commits = [line for line in output.split('\n') if line.strip()]
    return len(commits)

def create_contribution_log(repo_dir, count=1):
    log_file = os.path.join(repo_dir, "CONTRIBUTIONS.md")
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            f.write("# Daily GitHub Contribution Log\n\nTrack active development days and streak metrics.\n\n| Date & Time | Contribution Event | Status |\n|---|---|---|\n")

    created = 0
    for i in range(count):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"| {timestamp} | Activity check #{i+1} | ✅ Green Streak |\n"
        with open(log_file, "a") as f:
            f.write(entry)
        
        get_git_output("git add CONTRIBUTIONS.md", cwd=repo_dir)
        commit_msg = f"chore(streak): log daily contribution #{i+1} [{timestamp}]"
        get_git_output(f'git commit -m "{commit_msg}"', cwd=repo_dir)
        created += 1

    print(f"[SUCCESS] Created {created} contribution commit(s) in {repo_dir}")

def main():
    parser = argparse.ArgumentParser(description="GitHub Streak Keeper & Contribution Booster")
    parser.add_argument("--repo", default=os.getcwd(), help="Repository path")
    parser.add_argument("--count", type=int, default=7, help="Number of contributions to generate")
    parser.add_argument("--check", action="store_true", help="Check today's commit count")

    args = parser.parse_args()

    print("==========================================")
    print("🔥 GITHUB STREAK KEEPER CLI - @Vivekjpoojary")
    print("==========================================")

    today_count = check_today_contributions(args.repo)
    print(f"📅 Today's commits logged: {today_count}")

    if args.check:
        if today_count >= 7:
            print("✅ Great job! 7+ contributions recorded today. GitHub is GREEN!")
        else:
            print(f"⚠️ {today_count}/7 contributions so far today.")
        return

    if today_count < args.count:
        needed = args.count - today_count
        print(f"🚀 Generating {needed} additional structured contribution logs...")
        create_contribution_log(args.repo, count=needed)
    else:
        print(f"🎉 Already have {today_count} contributions today. Streak active!")

if __name__ == "__main__":
    main()
