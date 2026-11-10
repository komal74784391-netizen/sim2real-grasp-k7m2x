import argparse
import yaml

from src.affordance.model import AffordancePredictor
from src.sim.pretrain import domain_randomization


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='configs/corl.yaml')
    args = parser.parse_args()
    with open(args.config) as fh:
        cfg = yaml.safe_load(fh)
    model = AffordancePredictor()
    print('pretraining affordance model', cfg['train']['epochs'], 'epochs')


if __name__ == '__main__':
    main()
