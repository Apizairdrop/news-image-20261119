# The World in One Day — Thursday 19 November 2026

[![Competition](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/Apizairdrop/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![Reward](https://make.fun/badge/news-image-20261119/Apizairdrop/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

A newspaper front page that sums up the world news of **Thursday 19 November 2026** in a single image. Entry for the [make.fun competition `news-image-20261119`](https://make.fun/bounty/news-image-20261119).

## What the image shows

The front page leads with the day's biggest diplomatic story and carries three more below it, plus a ticker of two further stories:

1. **Shenzhen — Trump, Xi and Putin meet in first three-way summit.** The leaders of the United States, China and Russia met on the sidelines of the APEC forum in Shenzhen, holding 90 minutes of talks and announcing a joint peace declaration.
2. **The Hague — World court rules Myanmar committed genocide.** The International Court of Justice delivered its first genocide ruling, on the Rohingya case brought by Gambia.
3. **Ukraine war — Ukraine strikes Crimean Bridge for third time in a week.** A road span fell and road traffic was halted, while rail traffic kept running.
4. **New York — Van Gogh sells for $190.4m, a record for the artist.** *Chestnut Trees in Blossom* (1890) sold at Sotheby's on Wednesday.

The footer ticker adds two more stories of the day: COP31 climate talks racing on in Antalya, and Cyclone Akvan nearing India's east coast.

## How it was made

The four panel illustrations are original artwork generated for this entry — no news photographs or copied artwork are used. They were composed into the 1024×1024 front page with Python (Pillow), with all headlines, kickers, the date line and the ticker typeset in the build so the text stays crisp and legible even at small sizes.

## How to run it

Requires Python 3.13 (standard library only) and the `entry.png` file next to the script:

```sh
python3 main.py
```

The program validates `entry.png` — a whole PNG with every chunk checksum checked, at most 1 MiB and at most 1024×1024 pixels — and copies it byte-for-byte to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set). It re-reads the copy and checks it matches before finishing.

## Files

- `entry.png` — the finished front page (1024×1024)
- `main.py` — validator and copier
- `LICENSE` — MIT

## License

MIT. See `LICENSE`.
