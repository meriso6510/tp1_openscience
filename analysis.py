{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO2zIabltLwMWDCa1XjtXRC"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "Z0MhUCp6q-mG"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "df = pd.read_csv(\"data.csv\")\n",
        "\n",
        "print(\"Mean:\", df[\"value\"].mean())\n",
        "print(\"Standard deviation:\", df[\"value\"].std())\n",
        "\n",
        "df.plot(kind='bar', x='sample', y='value')\n",
        "plt.show()()"
      ]
    }
  ]
}