import pandas
import json
import hashlib
import sys

if len(sys.argv) == 2:

    csvfile = sys.argv[1]
else :
    print("Please enter a csv file")

    exit(2)



def generate_hash(csvfile):

    
    df = pandas.read_csv(csvfile)

    data = {}

    for (index, row) in df.iterrows():
        df_tmp = {
            row.Filename: {
                "format": "CHIP-0007",
                "name": row.Filename,
                "minting_tool": "Team-X",
                "sensitive_content": False,
                "series_number": row['Series Number'],
                "series_total": 1000,
                "attributes": [
                    {
                        "trait_type": "gender",
                        "value": row.Gender
                    },

                    {
                        "trait_type": "hair",
                        "value": row.Attributes.split(';')[0].split(':')[1]
                    },
                    {
                        "trait_type": "eyes",
                        "value": row.Attributes.split(';')[1].split(':')[1]
                    },
                    {
                        "trait_type": "teeth",
                        "value": row.Attributes.split(';')[2].split(':')[1]
                    },
                    {
                        "trait_type": "clothing",
                        "value": row.Attributes.split(';')[3].split(':')[1]
                    },
                    {
                        "trait_type": "accessories",
                        "value": row.Attributes.split(';')[4].split(':')[1]
                    },
                    {
                        "trait_type": "mask",
                        "value": row.Attributes.split(';')[5].split(':')[1]
                    },
                    {
                        "trait_type": "strength",
                        "value": row.Attributes.split(';')[6].split(':')[1]
                    },
                    {
                        "trait_type": "weakness",
                        "value": row.Attributes.split(';')[6].split(':')[1]
                    },
                ],  "collection": {
                    "name": "Zuri NFT Tickets for Free Lunch",
                    "id": row.UUID,
                    "attributes": [
                        {
                            "type": "description",
                            "value": "Rewards for accomplishments during HNGi9."
                        }
                    ]
                }
            }
        }


    data.update(df_tmp)

    with open(f"{row.Filename}.json", 'w') as f:
        json.dump(data, f, indent=4)

    
    encrypt = hashlib.sha256()

    with open(f"{row.Filename}.json", 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            encrypt.update(byte_block)
        hash = encrypt.hexdigest()

        df2 = pandas.read_csv(csvfile)

        for (index,row) in df2.iterrows():
            df2.loc[index, 'hash'] = hash

        df2.to_csv(f"{csvfile.rstrip('.csv')}.output.csv")

if __name__ == '__main__':
    generate_hash(csvfile)
