# Solution to Turing's Enigma Round 1

- Starting Point: [drive link](https://drive.google.com/drive/folders/1hrDN7JSfZb1pl1biYOahUcUlfWfvp_i4)
- Time: 1 hr 45 min

## Folder Structure

### ./data/folder_nothingtoseehere/

Objective is to unlock the encrypted rar archive

- **Password hints:**
  - tisu
  - FUSION25
  - MODULE
  - key to something: Turing's
  - module hint: take a break and appreciate the decor -> QR codes leading to a drive link and rick rolls
  - @btc

- **Methods:**
  - Inspect element was the most helpful as answers were present in the html files
  - some required basic math/CS knowledge and some puzzle solving skills
  - brute force attackers for simple ciphers online such as: [d code](https://www.dcode.fr/en)
  - I forgot the others and will add more resources later

- **Password:**
  `TURINGS_EN4GMA_FUSION25_@BTC_TISU_GREAT_MODULE`

- **Instructions:**

  - Use the password to decompress the [RAR file](./data/folder_nothingtoseehere/%D8%AF%D8%B9%20%D8%A7%D9%84%D8%A3%D9%84%D8%B9%D8%A7%D8%A8%20%D8%AA%D8%A8%D8%AF%D8%A3.rar) and obtain a PDF.
  - The PDF contains ciphertext colored white, making it look like the background in [extracted pdf](./data/folder_nothingtoseehere/%D8%AF%D8%B9%20%D8%A7%D9%84%D8%A3%D9%84%D8%B9%D8%A7%D8%A8%20%D8%AA%D8%A8%D8%AF%D8%A3.pdf)

  ### Message

  At the middle and end of the pdf what is apparently whitespace has the following text

  - First one is in [pdf cipher.txt](./data/folder_nothingtoseehere/pdf%20cipher.txt)

  - Second one is in [pdf cipher 2.txt](./data/folder_nothingtoseehere/pdf%20cipher%202.txt)

### ./data//QR codes/whydidyouscandecorework/

Objective is to get the email on which we have to submit the flag

- **QR Codes:**
  Lead to data in `./QR codes`.
  - [Drive link](https://drive.google.com/drive/folders/1QFHcifSk2lUqn3JcfZYawoHJAzlAOBdf)
  - [Surprise](https://www.youtube.com/watch?v=dQw4w9WgXcQ) - yes this happened

- **Email hints:**

  - og
  - challenge
  - numina
  - module

- **Email:**

  ```plaintext
  numinachallenge_og_module
  ```

## Flag

- I failed to find the flag, ill try again later some other time

## Objective

Email the flag to the email in designated time before others

## DISCLAIMER

None of the data that was provided as part of the event belongs to me and the only file I made in this directory (`src/Round1`) is the README for the solution and the directory `src/ciphers`. All of its credit goes to the Beaconhouse Tipu Sultan's CS module host team which organized this amazing event.
