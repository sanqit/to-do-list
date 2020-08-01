def congratulations(manager, tester, *developers):
    print("Happy New Year! Take care of yourself and your loved ones!")
    print("For:")
    for name in (manager, tester) + developers:
        print(name)
