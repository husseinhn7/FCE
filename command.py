ls  = { "name" : "ls",
    "help" : "Lists all the files that will be published/packaged",
    "options" : [
        {"flag" : "-s"  , "fullFlag" : "--yarn" , "help" : "Use yarn instead of npm (default inferred from presence of yarn.lock or .yarnrc)" },
        {"flag" : "-s1" , "fullFlag" : "--no-yarn" , "help" : "Use npm instead of yarn (default inferred from absence of yarn.lock or .yarnrc)" },
        {"flag" : "-s2" , "fullFlag" : "--packagedDependencies" , "help" : "Select packages that should be published only (includes dependencies)" },
        {"flag" : "-s3" , "fullFlag" : "--ignoreFile <path>" , "help" : " Indicate alternative .vscodeignore" },
        {"flag" : "-s4" , "fullFlag" : "--dependencies" , "help" : "Enable dependency detection via npm or yarn" },
        {"flag" : "-s5" , "fullFlag" : "--no-dependencies" , "help" : "Disable dependency detection via npm or yarn" },
    ]
}

pack = { "name" : "pack",
    "help" : "Packages an extension",
    "options" : [
        {"flag" : "-o"  , "fullFlag" : "--out <path>" , "help" : "Output .vsix extension file to <path> location (defaults to <name>-<version>.vsix)" },
        {"flag" : "-t"  , "fullFlag" : "--target" , "help" : "Use npm instead of yarn (default inferred from absence of yarn.lock or .yarnrc)" },
        {"flag" : "-s2" , "fullFlag" : "--ignore-other-target-folders" , "help" : "Ignore other target folders. Valid only when --target <target> is provided." },
        {"flag" : "-s3" , "fullFlag" : "--readme-path <path>" , "help" : "Path to README file (defaults to README.md)" },
        {"flag" : "-s4" , "fullFlag" : "--changelog-path <path>" , "help" : "Path to CHANGELOG file (defaults to CHANGELOG.md)" },
        {"flag" : "-m"  , "fullFlag" : "--message <commit message>" , "help" : "Commit message used when calling `npm version`." },
        
        {"flag" : "-o"  , "fullFlag" : "--no-git-tag-version" , "help" : "Do not create a version commit and tag when calling `npm version`. Valid only when[version] is provided." },
        {"flag" : "-t"  , "fullFlag" : "--no-update-package-json" , "help" : "Do not update `package.json`. Valid only when [version] is provided." },
        {"flag" : "-s2" , "fullFlag" : "--githubBranch <branch>" , "help" : "The GitHub branch used to infer relative links in README.md. Can be overridden by--baseContentUrl and --baseImagesUrl." },
        {"flag" : "-s3" , "fullFlag" : "--gitlabBranch <branch>" , "help" : "The GitLab branch used to infer relative links in README.md. Can be overridden by--baseContentUrl and --baseImagesUrl." },
        {"flag" : "-s4" , "fullFlag" : "--no-rewrite-relative-links" , "help" : "Skip rewriting relative links." },
        {"flag" : "-m"  , "fullFlag" : "--baseContentUrl <url>" , "help" : "Prepend all relative image links in README.md with the specified URL." },
        
        {"flag" : "-o"  , "fullFlag" : "--baseImagesUrl <url>" , "help" : "Prepend all relative image links in README.md with the specified URL." },
        {"flag" : "-t"  , "fullFlag" : "--yarn" , "help" : "Use yarn instead of npm (default inferred from presence of yarn.lock or .yarnrc)" },
        {"flag" : "-s2" , "fullFlag" : "--no-yarn" , "help" : "Use npm instead of yarn (default inferred from absence of yarn.lock or .yarnrc)" },
        {"flag" : "-s3" , "fullFlag" : "--ignoreFile <path>" , "help" : "Indicate alternative .vscodeignore" },
        {"fullFlag" : "--no-gitHubIssueLinking"     ,  "help"  : "Disable automatic expansion of GitHub-style issue syntax into links"},
        {"fullFlag" : "--no-gitLabIssueLinking"     ,  "help"  : "Disable automatic expansion of GitLab-style issue syntax into links"},
        {"fullFlag" : "--dependencies"              ,  "help"  : "Enable dependency detection via npm or yarn"},
        {"fullFlag" : "--no-dependencies"           ,  "help"  : "Disable dependency detection via npm or yarn"},
        {"fullFlag" : "--pre-release"               ,  "help"  : "Mark this package as a pre-release"},
        {"fullFlag" : "--allow-star-activation"     ,  "help"  : "Allow using * in activation events"},
        {"fullFlag" : "--allow-missing-repository"  ,  "help"  : "Allow missing a repository URL in package.json"},
        {"fullFlag" : "--skip-license"              ,  "help"  : "Allow packaging without license file"}
        
    ]
}

publish ={
    "name"  :  "publish",
    "help" : "Publishes an extension",
    "options" :[      
            {"fullFlag" : "-p, --pat <token>" ,               "help" :                "Personal Access Token (defaults to VSCE_PAT environment variable)" },
            {"fullFlag" : "-t, --target <targets...>" ,       "help" :        "Target architectures. Valid targets: win32-x64, win32-arm64, linux-x64, linux-arm64,linux-armhf, darwin-x64, darwin-arm64, alpine-x64, alpine-arm64, web" },
            {"fullFlag" : "--ignore-other-target-folders" ,   "help" :    "Ignore other target folders. Valid only when --target <target> is provided." },
            {"fullFlag" : "--readme-path <path>" ,            "help" :             "Path to README file (defaults to README.md)" },
            {"fullFlag" : "--changelog-path <path>" ,         "help" :          "Path to CHANGELOG file (defaults to CHANGELOG.md)" },
            {"fullFlag" : "-m, --message <commit message>" ,  "help" :   "Commit message used when calling `npm version`." },
            {"fullFlag" : "--no-git-tag-version" ,            "help" :             "Do not create a version commit and tag when calling `npm version`. Valid only when[version] is provided." },
            {"fullFlag" : "--no-update-package-json" ,        "help" :         "Do not update `package.json`. Valid only when [version] is provided." },
            {"fullFlag" : "-i, --packagePath <paths...>" ,    "help" :     "Publish the provided VSIX packages." },
            {"fullFlag" : "--githubBranch <branch>" ,         "help" :          "The GitHub branch used to infer relative links in README.md. Can be overridden by--baseContentUrl and --baseImagesUrl." },
            {"fullFlag" : "--gitlabBranch <branch>" ,         "help" :          "The GitLab branch used to infer relative links in README.md. Can be overridden by--baseContentUrl and --baseImagesUrl." },        
            {"fullFlag" : "--baseContentUrl <url>"          , "help" : "Prepend all relative links in README.md with the specified URL."},
            {"fullFlag" : "--baseImagesUrl <url>"           , "help" : "Prepend all relative image links in README.md with the specified URL."},
            {"fullFlag" : "--yarn"                          , "help" : "Use yarn instead of npm (default inferred from presence of yarn.lock or .yarnrc)"},
            {"fullFlag" : "--no-yarn"                       , "help" : "Use npm instead of yarn (default inferred from absence of yarn.lock or .yarnrc)"},
            {"fullFlag" : "--noVerify"                      , "help" : "Allow all proposed APIs (deprecated: use --allow-all-proposed-apis instead"},
            {"fullFlag" : "--allow-proposed-apis <apis...>" , "help" : "Allow specific proposed APIs"},
            {"fullFlag" : "--allow-all-proposed-apis"       , "help" : "Allow all proposed APIs"},
            {"fullFlag" : "--ignoreFile <path>"             , "help" : "Indicate alternative .vscodeignore"},
            {"fullFlag" : "--dependencies"                  , "help" : "Enable dependency detection via npm or yarn"},
            {"fullFlag" : "--no-dependencies"               , "help" : "Disable dependency detection via npm or yarn"},
            {"fullFlag" : "--pre-release"                   , "help" : "Mark this package as a pre-release"},
            {"fullFlag" : "--allow-star-activation"         , "help" : "Allow using * in activation events"},
            {"fullFlag" : "--allow-missing-repository"      , "help" : "Allow missing a repository URL in package.json"},
            {"fullFlag" : "--skip-duplicate"                , "help" : "Fail silently if version already exists on the marketplace"},
            {"fullFlag" : "--skip-license"                  , "help" : "Allow publishing without license file"},
        
    ]
}

unpublish = {
    "name" : "unpublish",
    "help" : "Unpublishes an extension. Example extension id: ms-vscode.live-server.",
    "options" : [
        {"fullFlag" : "-p, --pat <token>" , "help" : "Personal Access Token"},
        {"fullFlag" : "-f, --force"       , "help" : "Skip confirmation prompt when unpublishing an extension"},
        {"fullFlag" : "-h, --help"        , "help" : "display help for command"},
    ]
}

ls_publishers =  {
    "name" : "ls-publishers",
    "help" : "Lists all known publishers",
    "options" : []
}

delete_publisher = {
    "name" : "delete-publisher",
    "help" : "Deletes a publisher from marketplace",
        "options" : []

}

login  = {
    "name" : "login",
    "help" : "Adds a publisher to the list of known publishers",
        "options" : []

}

login  = {
    "name" : "login",
    "help" : "Adds a publisher to the list of known publishers",
        "options" : []

    
}

logout  = {
    "name" : "logout",
    "help" : "Removes a publisher to the list of known publishers",
        "options" : []

}

verify_pat  = {
    "name" : "verify-pat",
    "help" : "Verifies if the Personal Access Token has publish rights for the publisher",
    "options" : [ {"fullFlag" : "--pat <token>" , "help" : "Personal Access Token (defaults to VSCE_PAT environment variable)" }]
    
}

show = {
    "name" : "show",
    "help" : "Shows an extension's metadata",
    "options" : [{"fullFlag" : "--json" , "help"  :   "Outputs data in json format (default: false)"}]

}

search = {
    "name" : "search",
    "help" : "Searches extension gallery",
    "options" : [
        {"fullFlag" : "--json"  , "help"   :   "Outputs data in json format (default: false)"},
        {"fullFlag" : "--stats" , "help"   :   "Shows extensions rating and download count (default: false)"},
        {"fullFlag" : "-p, --pagesize [value]"  , "help"   :   "Number of results to return (default: '100')"},        
        ]

}



commands = [
    ls,
    pack,
    publish,
    unpublish,
    login,
    logout,
    ls_publishers,
    delete_publisher,
    verify_pat,
    show,
    search,
]



