from Function.funz_codifica import encode
from Function.funz_decodifica import decode

if __name__ == "__main__":
    print(encode("BRAVODAVIDE",25))
    print(decode("[kZoh]Zob]^",25))

    with open("Data\\data.txt","w") as file_data:
        file_data.write(encode("BRAVODAVIDE",25))
        file_data.write("\n"+decode("[kZoh]Zob]^",25))
    #file_data.close()  <---Non funziona
    