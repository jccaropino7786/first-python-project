import wikipedia

# Prompt the user for a search query
query = input("What would you like to search for on Wikipedia? ")

# Use the wikipedia library to search for the query
try:
    results = wikipedia.search(query)
    
    # Print out the titles of the top 5 search results
    for i, result in enumerate(results[:5]):
        print(f"{i+1}. {result}")
        
    # Prompt the user to select a page to view
    page_num = int(input("Enter the number of the page you would like to view: "))
    page_title = results[page_num-1]
    
    # Fetch the page content and print it out
    page_content = wikipedia.page(page_title).content
    print(page_content)
    
except wikipedia.exceptions.DisambiguationError as e:
    # If the search query is ambiguous, print out a list of options
    print("This search query is ambiguous. Please choose one of the following options:")
    for i, option in enumerate(e.options[:5]):
        print(f"{i+1}. {option}")
    option_num = int(input("Enter the number of the option you would like to choose: "))
    page_title = e.options[option_num-1]
    page_content = wikipedia.page(page_title).content
    print(page_content)