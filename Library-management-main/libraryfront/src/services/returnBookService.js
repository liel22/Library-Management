const BASE_URL = "http://localhost:5005";

/**
 * Return a borrowed book.
 *
 * @param {string} username - The ID of the user returning the book.
 * @param {string} title - The ID of the book to return.
 * @returns {Promise<object>} - Result with success and data/error details.
 */
export const returnBook = async (username, title) => {
  try {
    const response = await fetch(`${BASE_URL}/return-book`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username: username, title: title }),
    });

    if (response.ok) {
      const data = await response.json();
      return { success: true, data };
    } else {
      const error = await response.json();
      return {
        success: false,
        error: error.error || "Unknown error occurred.",
      };
    }
  } catch (error) {
    console.error("Error connecting to the service:", error.message);
    return {
      success: false,
      error: "Failed to connect to the return book service.",
    };
  }
};
