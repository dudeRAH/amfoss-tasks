#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <cs50.h>

#define UPPERCASE_LETTERS_START 65
#define LOWERCASE_LETTERS_START 97
#define LETTERS_COUNT 26

int main(int argc, string args[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar k");
        return 1;
    }

    int k = atoi(args[1]) % LETTERS_COUNT; // if k is > 26, store the division remainder instead
    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");

    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (!isalpha(plaintext[i]))
        {
            printf("%c", plaintext[i]);
            continue;
        }

        int ascii_offset = isupper(plaintext[i]) ? UPPERCASE_LETTERS_START : LOWERCASE_LETTERS_START;

        int pi = plaintext[i] - ascii_offset;
        int ci = (pi + k) % LETTERS_COUNT;

        printf("%c", ci + ascii_offset);
    }

    printf("\n");
    return 0;
}
