module.exports = function (eleventyConfig) {
    // Copy assets to output
    eleventyConfig.addPassthroughCopy("Lessons/**/*.{png,jpg,jpeg,gif,svg}");
    eleventyConfig.addPassthroughCopy("_site/css");
    eleventyConfig.addPassthroughCopy("_site/js");

    // Add collection for courses
    eleventyConfig.addCollection("courses", function (collectionApi) {
        return collectionApi.getFilteredByGlob("Lessons/*/README.md");
    });

    // Add date filter
    eleventyConfig.addFilter("dateFormat", function (date) {
        return new Date(date).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    });

    // Add reading time filter
    eleventyConfig.addFilter("readingTime", function (text) {
        const wordsPerMinute = 200;
        const numberOfWords = text.split(/\s+/).length;
        const minutes = Math.ceil(numberOfWords / wordsPerMinute);
        return `${minutes} min read`;
    });

    // Set markdown library options
    let markdownIt = require("markdown-it");
    let markdownItAnchor = require("markdown-it-anchor");
    let options = {
        html: true,
        breaks: true,
        linkify: true
    };

    let markdownLib = markdownIt(options).use(markdownItAnchor);
    eleventyConfig.setLibrary("md", markdownLib);

    // Configure syntax highlighting
    eleventyConfig.addPlugin(require("@11ty/eleventy-plugin-syntaxhighlight"));

    // Configure BrowserSync to disable all reload functionality
    eleventyConfig.setBrowserSyncConfig({
        notify: false,  // Disable the notification overlay
        ui: false,      // Disable the BrowserSync UI
        ghostMode: false,  // Disable syncing across devices
        open: false,    // Don't auto-open browser
        reloadDelay: 0,
        reloadDebounce: 0,
        injectChanges: false,  // Don't inject CSS changes
        codeSync: false,  // Disable code syncing
        snippetOptions: {
            rule: {
                match: /<\/body>/i,
                fn: function (snippet, match) {
                    // Inject custom script to completely block reload dialogs
                    return '<script>if(window.___browserSync___){window.___browserSync___.socket.on=function(){};}</script>' + match;
                }
            }
        },
        callbacks: {
            ready: function (err, bs) {
                // Disable reload confirmations at the source
                bs.options.set('notify', false);
                bs.options.set('reloadDelay', 0);
            }
        }
    });

    return {
        dir: {
            input: "Lessons",
            output: "_site",
            includes: "../_includes"
        },
        templateFormats: ["md", "njk", "html"],
        markdownTemplateEngine: "njk",
        htmlTemplateEngine: "njk",
        dataTemplateEngine: "njk"
    };
};
