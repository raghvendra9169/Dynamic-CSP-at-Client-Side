# Dynamic Content Security Policy Generation at Browser-Side to Mitigate XSS Attacks
Cross-site scripting (XSS) attacks are a major threat to web applications and have consistently ranked among the
[OWASP Top 10](https://owasp.org/www-project-top-ten/) vulnerabilities. Attackers can inject malicious scripts that execute within a user’s browser. Server side Content Security Policies (CSPs) offer some protection, but their static nature makes them ineffective when dealing with dynamic content and a very small percentage of web application use. This
project explores dynamically generated CSPs on the client side.

## Introduction
The World Wide Web, or Web, is used for communication, commerce, entertainment, and other sectors. It consists of interconnected hypertext documents accessed through the Internet. Every web service uses the [client-server architecture.](https://en.wikipedia.org/wiki/Client%E2%80%93server_model) On the web, several attacks are possible. [Cross-site scripting (XSS) attacks are a major threat to web applications.](https://ieeexplore.ieee.org/document/8597221)

### XSS Attacks and its types:
Cross-Site Scripting (XSS) attacks are a type of web security vulnerability that allows attackers to inject malicious scripts into otherwise trusted website. For more detail you can see these paper [Mitigating Cross-Site Scripting Attacks with a Content Security Policy](https://ieeexplore.ieee.org/document/7433336) , [A Survey of Exploitation and Detection Methods of XSS Vulnerabilities](https://ieeexplore.ieee.org/document/8935148).

XSS attacks is three types:

  - Stored XSS: Malicious script is stored on the server (e.g., in a database).

  - Reflected XSS: Malicious script is reflected off a web server, usually via a URL.

  -  Dom-Based XSS: Malicious script is executed as a result of modifying the [DOM environment](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) in the client-side code.

### XSS Mitigation Methods:
Following are the the list of XSS mitigation methods:

  -  Input Validation & Sanitization: Ensure inputs are properly validated and sanitized.

  -  Output Encoding: Encode all user-controlled data before displaying it on the web page to prevent it from being interpreted as code.

  -  Content Security Policy (CSP): Set browser restrictions to only allow scripts from trusted sources,
limiting potential harm from malicious injections.

  -  HttpOnly & Secure Flags for Cookies: Mitigate theft of sensitive cookies stored by the browser.

  -  Regular Security Testing:  Proactively identify and patch vulnerabilities in your web application to     minimize attack opportunities.
  
  -  Use of Secure Frameworks: Leverage frameworks that automatically handle XSS.

## Introduction to Content Security Policy (CSP)

-  Why is the content security policy better than other methods?  [Content Security Policy (CSP)](https://www.w3.org/TR/CSP3/) is better because: It provides a comprehensive approach to security by specifying which sources of content are allowed. It can mitigate multiple types of attacks beyond XSS, including data injection. It is a flexible, defense-in-depth strategy that complements other security measures.

-  What is the content security policy? Content Security Policy (CSP) is a security feature that helps prevent attacks by specifying which content sources are trusted. It’s like a whitelist for what your web page is allowed to load and execute, protecting against malicious scripts.

-  How CSP Policy Delivery, Policy Enforcement: Content Security Policy (CSP) is a security feature that helps prevent various types of attacks by specifying which sources of content are trusted.

- [- **Policy Delivery:**](https://www.w3.org/TR/CSP3/) Delivered via HTTP headers (Content-Security-Policy). It Can also be delivered via <meta> tags in HTML.

- [- **Policy Enforcement:**](https://www.w3.org/TR/CSP3/)  Enforced by the browser, which blocks content that violates the specified policy. Policies can be set to "report-only" mode for testing without enforcement, using Content-Security-Policy-Report-Only.

### Demonstration of CSP & XSS Attacks

- **A website with and witout CSP:** Here, we can compare two versions of a simple website: One [with](https://github.com/brcnitk/PG-23-24-Raghavendra/tree/main/Major%20Project/example_xss_csp/hello_with_csp.py) a Content Security Policy (CSP) implemented. Another [without](https://github.com/brcnitk/PG-23-24-Raghavendra/tree/main/Major%20Project/example_xss_csp/hello.py) a CSP.
To check whether CSP is present on a website, there are two methods: (i) Using Browser Developer Tools. (ii) Checking for Meta Tags

- Run these files using the [Python Flask framework](https://flask.palletsprojects.com/en/3.0.x/)  [(instructions on how to run them are provided).](https://github.com/brcnitk/PG-23-24-Raghavendra/tree/main/Major%20Project/example_xss_csp/)  To verify the CSP policy see [this directory](https://github.com/brcnitk/PG-23-24-Raghavendra/tree/main/Major%20Project/example_xss_csp/). It explains step by step process to check csp header

- In the [figure below](https://github.com/brcnitk/PG-23-24-Raghavendra/blob/main/Major%20Project/images/example_csp.png)
, the HTTP response header shows a Content Security Policy (CSP) in the third entry (as seen on the left side of the image). However, the right side of the image appears to lack a CSP policy.

  
![CSP Header Generation](https://github.com/brcnitk/PG-23-24-Raghavendra/blob/main/Major%20Project/images/example_csp.png)

**Example of XSS attack:**

- [This folder](https://github.com/brcnitk/PG-23-24-Raghavendra/tree/main/Major%20Project/example_xss_csp/) contains a file demonstrating all three types of XSS attacks. The file, [xss.py](https://github.com/brcnitk/PG-23-24-Raghavendra/tree/main/Major%20Project/example_xss_csp/xss.py), provides examples of these attacks. Instructions on how to run [xss.py](https://github.com/brcnitk/PG-23-24-Raghavendra/tree/main/Major%20Project/example_xss_csp/xss.py) can be found in [this folder.](https://github.com/brcnitk/PG-23-24-Raghavendra/tree/main/Major%20Project/example_xss_csp)


## CSP at Browser

### Introduction to Browser Framework 
A web browser is a software application that allows you to access and interact with information on the World Wide Web (WWW). It acts as an intermediary between you and the web servers that store websites. [General components of the browser](https://www.browserstack.com/guide/browser-rendering-engine) is explained here.

![Browser](https://github.com/brcnitk/PG-23-24-Raghavendra/blob/main/Major%20Project/images/arch_browser.png)

- **User Interface (UI):** This is the part you interact with directly. It includes elements like the address bar, back and forward buttons, bookmarks, and the area that displays the web page content.

- **Browser Engine:** This component acts as the control center of the browser. It receives user input from the UI and fetches web content from the internet using the networking layer. It also communicates with the rendering engine to display the fetched content.

- **Rendering Engine:** This engine is responsible for interpreting the web content (HTML, CSS, JavaScript) and turning it into a visually appealing webpage on your screen. It parses the HTML code, applies the CSS styles, and executes any JavaScript code to generate the final layout and content.
  
- **Networking Layer:** This layer handles communication between the browser and the internet. It uses protocols like HTTP and HTTPS to request web pages and other resources from servers.
  
- **JavaScript Engine:** Modern web pages often use JavaScript to create dynamic and interactive features. The JavaScript engine is responsible for interpreting and executing JavaScript code, allowing web pages to be more responsive and engaging.

- **Data Persistence (Storage):** This component manages how the browser stores data locally on your device. This can include things like cookies, cache, and offline data. Cookies are used to remember user preferences and browsing history, while the cache stores frequently accessed resources to improve loading times.

- **UI backend:**  UI backend also sometimes called the graphics layer or widget toolkit plays a crucial role behind the scenes in rendering the user interface.



### Generation of CSP 
When you interact with a web application, your browser sends requests following HTML structure.  CSS styles it for presentation, and JavaScript might handle interactive elements.  On the back-end, the web server receives the request, the server-side script processes it, potentially interacts with a database, and generates a response that's sent back to your browser. The browser interprets this response and updates the web page accordingly. To generate the CSP at browser side following are steps:

- Fetch HTML Content: This step retrieves the HTML content of the searched webpage by using Python library [requests](https://pypi.org/project/requests/).
- Parse HTML: Use the [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) library to parse the searched HTML content. It essentially breaks down the HTML structure into manageable pieces. And extracting the domains associated with various resources like scripts, stylesheets, and images. This is done by iterating through specific HTML tags (e.g., <script>, <link>, <img>) and identifying the source (src) or reference (href) attributes.  The get_domain function helps extract the domain name (e.g., "example.com") from the URL string if it exists.
- Initialize Default CSP Directives: This defines the baseline security policy for resources loaded by the webpage. Typically, a default CSP directive like "script-src": "'self'" is used. This allows scripts only from the same origin (the same domain as the webpage) to execute.
- Construct CSP: Create a CSP header string with the extracted domains and default security directives and return.
### Integration of CSP and Browser
- Monitor the outgoing HTTP requests from the browser.
- Intercept the HTTP responses before they reach the browser or application.
- Generate a CSP header based on the content and resources used in the response.
- Integrating the generated CSP header into the web browsing process. The browser will then enforce this policy, blocking any resources that don't comply with the defined directives.
- Send the generated CSP header into HTTP requests made by the web engine.
- Browser Integration: The browser is configured to enforce CSP rules. This involves enabling CSP support and ensuring the browser can parse and apply CSP headers.
- Resource Loading: When a web page requests resources (e.g., scripts, stylesheets), the browser checks the CSP directives. Allowed resources (specified by 'self', specific domains, or other criteria) are loaded. Disallowed resources are blocked, enhancing the security of the web page.
- Inline Script and Style Handling: Inline scripts and styles pose a security risk if not handled properly.The browser compares the hash or nonce of the inline content with the values specified in the CSP. Only matching content is executed.
Any attempts to load or execute disallowed resources are reported.
These reports are sent to a specified endpoint, allowing administrators to monitor and address security issues.


### Demonstration

Build a modular [PyQt5 browser](https://github.com/brcnitk/PG-23-24-Raghavendra/tree/main/Major%20Project/browser) with the following structure: create several modules, each handling a different aspect of the browser's functionality. These functionalities include setting up the main window, managing tabs, the toolbar, the URL bar, and optional features like history. And add a content security policy (CSP) generation feature based on the method explained above. You can find the implementation steps in this [folder](https://github.com/brcnitk/PG-23-24-Raghavendra/tree/main/Major%20Project/browser). 

- When locally hosted a website and accessed it, it generated a Content Security Policy (CSP) header. Similarly, another website hosted on the cloud also generated a CSP header.


![Policy Enforcement](https://github.com/brcnitk/PG-23-24-Raghavendra/blob/main/Major%20Project/images/multiple_csp.png)

- When I searched a wkipeadia website, it generated a Content Security Policy (CSP) header. We can see in below [figure.](https://github.com/brcnitk/PG-23-24-Raghavendra/blob/main/Major%20Project/images/brow_csp.png)

![Policy Enforcement](https://github.com/brcnitk/PG-23-24-Raghavendra/blob/main/Major%20Project/images/brow_csp.png)

- When I searched a another website, it generated a Content Security Policy (CSP) header. We can see in below [figure.](https://github.com/brcnitk/PG-23-24-Raghavendra/blob/main/Major%20Project/images/brow_csp2.0.png)



![Policy Enforcement](https://github.com/brcnitk/PG-23-24-Raghavendra/blob/main/Major%20Project/images/brow_csp2.0.png)
