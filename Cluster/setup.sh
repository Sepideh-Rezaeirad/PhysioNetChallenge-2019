#!/bin/bash
#SBATCH --nodes=1
#SBATCH --mem=100G
#SBATCH --partition=sched_mit_rgmark
#SBATCH --time=100:00:00
#SBATCH --job-name=AdaBoost
#SBATCH --mail-type=ALL
#SBATCH --mail-user=sepideh.rezaeerad@gmail.com
#SBATCH --output=test1.%j.out
#SBATCH --error=test1.%j.err


. /etc/profile.d/modules.sh
module load python/3.6.3
module load cuda/9.0
module load cudnn/7.5.1


virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt



python Main.py