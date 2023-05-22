class Funcion:

    #Cuenta las a's totales del fichero
    def count_a(self,frase):
        count= frase.lower().count('a')
        return count
    def palindromas(self,frase):
        palabras =frase.split()
        palindromas = [palabra for palabra in palabras if palabra.lower() == palabra.lower()[::-1]]
        return palindromas

    def capicuas(self,frase):
        numeros= [palabra for palabra in frase.split() if palabra.isdigit()]
        capicua = [num for num in numeros if num == num[::-1]]
        return capicua
