with open('spam.tc', 'a+') as file:
    counter = 0
    with open('upper_wordlist_bi_clean.txt', 'r') as bfile:
        bagofwords = bfile.readlines()
        for item in bagofwords:
            file.write("WebUI.setText(findTestObject('Object Repository/Success/div_Test 4'), '{}')\n".format(item.rstrip()))
            file.write("WebUI.click(findTestObject('Object Repository/Success/i__c-icon c-icon--paperplane-filled'))\n")
            print(item.rstrip())
            counter += 1
            print(counter)
            if counter == 30000:
                exit(0)
