// google_translate.js

// Set cookie
function setCookie(name, value, days) {
    let expires = "";
    if (days) {
      const date = new Date();
      date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
      expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
  }
  
  // Get language from cookie
  function getLanguageFromCookie() {
    const match = document.cookie.match(/googtrans=\/en\/([\w-]+)/);
    return match ? match[1] : "en";
  }
  
  // Apply translation based on cookie
  function setLanguageFromCookie() {
    const lang = getLanguageFromCookie();
    const script = document.createElement("script");
    script.src = "//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit";
    document.body.appendChild(script);
  
    window.googleTranslateElementInit = () => {
      new google.translate.TranslateElement({
        pageLanguage: "en",
        includedLanguages: "en,hi,ta,te,ml,bn,mr,gu,pa,kn",
        layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
        autoDisplay: false,
      }, "google_translate_element");
    };
  }
  
  // Handle dropdown change
  function handleLanguageChange() {
    const dropdown = document.getElementById("languageDropdown");
    if (dropdown) {
      const lang = dropdown.value;
      setCookie("googtrans", `/en/${lang}`, 1);
      location.reload();
    }
  }
  
  // Pre-select dropdown on load
  function preselectLanguageDropdown() {
    const lang = getLanguageFromCookie();
    const dropdown = document.getElementById("languageDropdown");
    if (dropdown) dropdown.value = lang;
  }
  
  // Execute on load
  window.onload = () => {
    setLanguageFromCookie();
    preselectLanguageDropdown();
  };
  