def test_api_get(playwright):
    request = playwright.request.new_context()
    response = request.post(
        "https://jsonplaceholder.typicode.com/posts",
        data={"title": "qui est esse"}
    )
    assert response.status == 201
    print(response.json())
    request.dispose()