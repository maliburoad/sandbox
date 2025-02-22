def main():
    """business logic for when running this module as the primary one!"""
    setup()
    foo = do_important()
    bar = do_even_more_important(foo)
    for baz in bar:
        do_super_important(baz)
    teardown()

# Here's our payoff idiom!
if __name__ == '__main__':
    main()