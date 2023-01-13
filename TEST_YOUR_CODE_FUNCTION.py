def my_challenge_function(args):
    return

def testing(function_vals, wanted_result: list):
    if function_vals == wanted_result:
        print('Test passed, {} == {}'.format(function_vals,wanted_result))
    else:
        print('Test failed, {} =/= {}'.format(function_vals,wanted_result))

testing(my_challenge_function('values to test your function with'), 'values that you should get')
