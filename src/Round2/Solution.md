# Solution to Turing's Enigma Round 2

## Starting Point

- [Round 2 Start Document](../Round2/round%202%20start.pdf)
- Time: 1 hour 45 minutes

## Social Media Accounts

- **Instagram:** [stemfusion_meme_page](https://www.instagram.com/stemfusion_meme_page/)

    hinted in the starting document and new page

- **Github:** [stem-memer](https://github.com/stem-memer/stem-memer)

    From a Story Uploaded on Instagram, the GitHub account's name could be seen

- **Email:** <stem.memer@gmail.com>

    Similarly, from a story uploaded to Instagram, the email could be seen

- **Deleted Accounts:**
  - Reddit
  - Twitter
  - Youtube Channel (maybe it was never made)

## Password Hints

for the encrypted rar archive

- WITHIN
- SECRETS
- WHISPERS
- DECODE
- AGENTS
- HIDDEN
- "Since when was 1942 not a great ending of a password" -comment on instagram
  - I found no use of this

- **Format:** `######_######_#######_######_######_########`

**PASSWORD:** AGENTS_DECODE_SECRETS_HIDDEN_WITHIN_WHISPERS

## Methods of Obtaining Hints

- **ExifTool:** [exif tool online](https://ezgif.com/) or [download](https://exiftool.org/)
  - Two Google Drive Links in metadata
  - Morse code in metadata to get another hint

- **Image Decoder:** [stenography online](https://stylesuxx.github.io/steganography/)
  - Changing the encoding of images present in the GitHub repo showed hints to the password

- Rest was just available online in the open.

## Flags

Indicated as stem.ctf{ }

1. **hello.world**
    - Located in git history of LOL.txt: [git history](https://github.com/stem-memer/stem-memer/commit/234ea453192f6dfaa392547b55883c6a8d6f0baa)
2. **you.are.a.fine.hacker**
    - Located in the encrypted rar: [extracted file](../Round2/flag.txt)

3. **Asset:**
    - [Image](../Round2/asset.jpg)

Flags were to be sent to the email along with the asset.

## DISCLAIMER

None of the data that was provided as part of the event belongs to me and the only file I made in this directory (`src/Round2`) is the README for the solution. All of its credit goes to the Beaconhouse Tipu Sultan's CS module host team which organized this amazing event.
