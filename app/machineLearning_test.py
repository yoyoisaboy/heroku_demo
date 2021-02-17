# -*- coding: utf-8 -*-
#https://machine-learning-python.kspax.io/datasets/ex4_plot_random_multilabel_dataset
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_multilabel_classification as make_ml_clf


COLORS = np.array(['!',
                   '#FF3333',  # red
                   '#0198E1',  # blue
                   '#BF5FFF',  # purple
                   '#FCD116',  # yellow
                   '#FF7216',  # orange
                   '#4DBD33',  # green
                   '#87421F'   # brown
                   ])

RANDOM_SEED = np.random.randint(2 ** 10)

def plot_2d(ax, n_labels=1, n_classes=3, length=50):
    X, Y, p_c, p_w_c = make_ml_clf(n_samples=150, n_features=2,
                                   n_classes=n_classes, n_labels=n_labels,
                                   length=length, allow_unlabeled=False,
                                   return_distributions=True,
                                   random_state=RANDOM_SEED)

    ax.scatter(X[:, 0], X[:, 1], color=COLORS.take((Y * [1, 2, 4]
                                                    ).sum(axis=1)),
               marker='.')
    ax.scatter(p_w_c[0] * length, p_w_c[1] * length,
               marker='*', linewidth=.5, edgecolor='black',
               s=20 + 1500 * p_c ** 2,
               color=COLORS.take([1, 2, 4]))
    ax.set_xlabel('Feature 0 count')
    return p_c, p_w_c

def test():
    _, (ax1, ax2) = plt.subplots(1, 2, sharex='row', sharey='row', figsize=(8, 4))
    plt.subplots_adjust(bottom=.15)
    
    p_c, p_w_c = plot_2d(ax1, n_labels=1)
    ax1.set_title('n_labels=1, length=50')
    ax1.set_ylabel('Feature 1 count')
    
    plot_2d(ax2, n_labels=3)
    ax2.set_title('n_labels=3, length=50')
    ax2.set_xlim(left=0, auto=True)
    ax2.set_ylim(bottom=0, auto=True)
    plt.savefig('./app/static/result_plot/result.png')
    return 'result.png'