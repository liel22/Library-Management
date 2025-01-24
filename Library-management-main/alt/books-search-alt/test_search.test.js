const request = require("supertest");
const app = require("./app"); // הנחה שהשירות שלך בקובץ index.js

describe("Search Service Tests", () => {
  test("Positive test: Search by title", async () => {
    const res = await request(app).get("/search").query({
      title: "Kobi The Great",
      author: "kobi",
      category: "great",
    });
    expect(res.statusCode).toBe(200);
    expect(res.body.books).toEqual(
      expect.arrayContaining([
        expect.objectContaining({
          title: "Kobi The Great",
          author: "kobi",
          category: "great",
        }),
      ])
    );
  });

  test("Negative test: Search with no matches", async () => {
    const res = await request(app).get("/search").query({
      title: "nonexistentbook",
      author: "nonexistentauthor",
      category: "nonexistentcategory",
    });
    expect(res.statusCode).toBe(404);
    expect(res.body.message).toBe("No books found matching the criteria");
  });
});
