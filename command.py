ls  = { "name" : "ls",
    "help" : "Lists all the files that will be published/packaged",
    "options" : [
        {"flag" : "-s"  ,"action" : "store_true"  , "fullFlag" :  "--yarn" , "help" : "Use yarn instead of npm (default inferred from presence of yarn.lock or .yarnrc)" },
        {"flag" : "-s1" ,"action" : "store_true"  , "fullFlag" :  "--no-yarn" , "help" : "Use npm instead of yarn (default inferred from absence of yarn.lock or .yarnrc)" },
        {"flag" : "-s2" ,"action" : "store_true"  , "fullFlag" :  "--packagedDependencies" , "help" : "Select packages that should be published only (includes dependencies)" },
        {"flag" : "-s3" ,"action" : "store_const" , "fullFlag" :  "--ignoreFile" , "help" : " Indicate alternative .vscodeignore" },
        {"flag" : "-s4" ,"action" : "store_true"  , "fullFlag" :  "--dependencies" , "help" : "Enable dependency detection via npm or yarn" },
        {"flag" : "-s5" ,"action" : "store_true"  , "fullFlag" :  "--no-dependencies" , "help" : "Disable dependency detection via npm or yarn" },
    ]
}

pack = { "name" : "pack",
    "help" : "Packages an extension",
    "options" : [
        {"flag" : "-o"  ,"action" : "store_true"  , "fullFlag" : "--out" , "help" : "Output .vsix extension file to <path> location (defaults to <name>-<version>.vsix)" },
        {"flag" : "-t"  ,"action" : "store_true"  , "fullFlag" : "--target" , "help" : "Use npm instead of yarn (default inferred from absence of yarn.lock or .yarnrc)" },
        {"flag" : "-s2" ,"action" : "store_true"  , "fullFlag" : "--ignore-other-target-folders" , "help" : "Ignore other target folders. Valid only when --target <target> is provided." },
        {"flag" : "-s3" ,"action" : "store_true"  , "fullFlag" : "--readme-path <path>" , "help" : "Path to README file (defaults to README.md)" },
        {"flag" : "-s4" ,"action" : "store_true"  , "fullFlag" : "--changelog-path <path>" , "help" : "Path to CHANGELOG file (defaults to CHANGELOG.md)" },
        {"flag" : "-m"  ,"action" : "store_true"  , "fullFlag" : "--message <commit message>" , "help" : "Commit message used when calling `npm version`." },       
        {"flag" : "-o"  ,"action" : "store_true"  , "fullFlag" : "--no-git-tag-version" , "help" : "Do not create a version commit and tag when calling `npm version`. Valid only when[version] is provided." },
        {"flag" : "-t"  ,"action" : "store_true"  , "fullFlag" : "--no-update-package-json" , "help" : "Do not update `package.json`. Valid only when [version] is provided." },
        {"flag" : "-s2" ,"action" : "store_true"  , "fullFlag" : "--githubBranch <branch>" , "help" : "The GitHub branch used to infer relative links in README.md. Can be overridden by--baseContentUrl and --baseImagesUrl." },
        {"flag" : "-s3" ,"action" : "store_true"  , "fullFlag" : "--gitlabBranch <branch>" , "help" : "The GitLab branch used to infer relative links in README.md. Can be overridden by--baseContentUrl and --baseImagesUrl." },
        {"flag" : "-s4" ,"action" : "store_true"  , "fullFlag" : "--no-rewrite-relative-links" , "help" : "Skip rewriting relative links." },
        {"flag" : "-m"  ,"action" : "store_true"  , "fullFlag" : "--baseContentUrl <url>" , "help" : "Prepend all relative image links in README.md with the specified URL." },        
        {"flag" : "-o"  ,"action" : "store_true"  , "fullFlag" : "--baseImagesUrl <url>" , "help" : "Prepend all relative image links in README.md with the specified URL." },
        {"flag" : "-t"  ,"action" : "store_true"  , "fullFlag" : "--yarn" , "help" : "Use yarn instead of npm (default inferred from presence of yarn.lock or .yarnrc)" },
        {"flag" : "-s2" ,"action" : "store_true"  , "fullFlag" : "--no-yarn" , "help" : "Use npm instead of yarn (default inferred from absence of yarn.lock or .yarnrc)" },
        {"flag" : "-s3" ,"action" : "store_true"  , "fullFlag" : "--ignoreFile <path>" , "help" : "Indicate alternative .vscodeignore" },
        {"action" : "store_true" , "fullFlag" : "--no-gitHubIssueLinking"     ,  "help"  : "Disable automatic expansion of GitHub-style issue syntax into links"},
        {"action" : "store_true" , "fullFlag" : "--no-gitLabIssueLinking"     ,  "help"  : "Disable automatic expansion of GitLab-style issue syntax into links"},
        {"action" : "store_true" , "fullFlag" : "--dependencies"              ,  "help"  : "Enable dependency detection via npm or yarn"},
        {"action" : "store_true" , "fullFlag" : "--no-dependencies"           ,  "help"  : "Disable dependency detection via npm or yarn"},
        {"action" : "store_true" , "fullFlag" : "--pre-release"               ,  "help"  : "Mark this package as a pre-release"},
        {"action" : "store_true" , "fullFlag" : "--allow-star-activation"     ,  "help"  : "Allow using * in activation events"},
        {"action" : "store_true" , "fullFlag" : "--allow-missing-repository"  ,  "help"  : "Allow missing a repository URL in package.json"},
        {"action" : "store_true" , "fullFlag" : "--skip-license"              ,  "help"  : "Allow packaging without license file"}
        
    ]
}

publish ={
    "name"  :  "publish",
    "help" : "Publishes an extension",
    "options" :[      
            {"action" : "store_true" , "fullFlag" : "--pat" ,               "help" :                "Personal Access Token (defaults to VSCE_PAT environment variable)" },
            {"action" : "store_true" , "fullFlag" : "-t, --target <targets...>" ,       "help" :        "Target architectures. Valid targets: win32-x64, win32-arm64, linux-x64, linux-arm64,linux-armhf, darwin-x64, darwin-arm64, alpine-x64, alpine-arm64, web" },
            {"action" : "store_true" , "fullFlag" : "--ignore-other-target-folders" ,   "help" :    "Ignore other target folders. Valid only when --target <target> is provided." },
            {"action" : "store_true" , "fullFlag" : "--readme-path <path>" ,            "help" :             "Path to README file (defaults to README.md)" },
            {"action" : "store_true" , "fullFlag" : "--changelog-path <path>" ,         "help" :          "Path to CHANGELOG file (defaults to CHANGELOG.md)" },
            {"action" : "store_true" , "fullFlag" : "-m, --message <commit message>" ,  "help" :   "Commit message used when calling `npm version`." },
            {"action" : "store_true" , "fullFlag" : "--no-git-tag-version" ,            "help" :             "Do not create a version commit and tag when calling `npm version`. Valid only when[version] is provided." },
            {"action" : "store_true" , "fullFlag" : "--no-update-package-json" ,        "help" :         "Do not update `package.json`. Valid only when [version] is provided." },
            {"action" : "store_true" , "fullFlag" : "-i, --packagePath <paths...>" ,    "help" :     "Publish the provided VSIX packages." },
            {"action" : "store_true" , "fullFlag" : "--githubBranch <branch>" ,         "help" :          "The GitHub branch used to infer relative links in README.md. Can be overridden by--baseContentUrl and --baseImagesUrl." },
            {"action" : "store_true" , "fullFlag" : "--gitlabBranch <branch>" ,         "help" :          "The GitLab branch used to infer relative links in README.md. Can be overridden by--baseContentUrl and --baseImagesUrl." },        
            {"action" : "store_true" , "fullFlag" : "--baseContentUrl <url>"          , "help" : "Prepend all relative links in README.md with the specified URL."},
            {"action" : "store_true" , "fullFlag" : "--baseImagesUrl <url>"           , "help" : "Prepend all relative image links in README.md with the specified URL."},
            {"action" : "store_true" , "fullFlag" : "--yarn"                          , "help" : "Use yarn instead of npm (default inferred from presence of yarn.lock or .yarnrc)"},
            {"action" : "store_true" , "fullFlag" : "--no-yarn"                       , "help" : "Use npm instead of yarn (default inferred from absence of yarn.lock or .yarnrc)"},
            {"action" : "store_true" , "fullFlag" : "--noVerify"                      , "help" : "Allow all proposed APIs (deprecated: use --allow-all-proposed-apis instead"},
            {"action" : "store_true" , "fullFlag" : "--allow-proposed-apis <apis...>" , "help" : "Allow specific proposed APIs"},
            {"action" : "store_true" , "fullFlag" : "--allow-all-proposed-apis"       , "help" : "Allow all proposed APIs"},
            {"action" : "store_true" , "fullFlag" : "--ignoreFile <path>"             , "help" : "Indicate alternative .vscodeignore"},
            {"action" : "store_true" , "fullFlag" : "--dependencies"                  , "help" : "Enable dependency detection via npm or yarn"},
            {"action" : "store_true" , "fullFlag" : "--no-dependencies"               , "help" : "Disable dependency detection via npm or yarn"},
            {"action" : "store_true" , "fullFlag" : "--pre-release"                   , "help" : "Mark this package as a pre-release"},
            {"action" : "store_true" , "fullFlag" : "--allow-star-activation"         , "help" : "Allow using * in activation events"},
            {"action" : "store_true" , "fullFlag" : "--allow-missing-repository"      , "help" : "Allow missing a repository URL in package.json"},
            {"action" : "store_true" , "fullFlag" : "--skip-duplicate"                , "help" : "Fail silently if version already exists on the marketplace"},
            {"action" : "store_true" , "fullFlag" : "--skip-license"                  , "help" : "Allow publishing without license file"},
        
    ]
}

unpublish = {
    "name" : "unpublish",
    "help" : "Unpublishes an extension. Example extension id: ms-vscode.live-server.",
    "options" : [
        {"action" : "store_true" , "fullFlag" : "-p, --pat" , "help" : "Personal Access Token"},
        {"action" : "store_true" , "fullFlag" : "-f, --force"       , "help" : "Skip confirmation prompt when unpublishing an extension"},
        {"action" : "store_true" , "fullFlag" : "-h, --help"        , "help" : "display help for command"},
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
        "options" : [
            {"action" : "store_true" , "fullFlag" : "--pat" , "help" : "Personal Access Token"},
            {"action" : "store_true" , "fullFlag" : "--pub"  , "help" : "name of the publisher"},    
        ]

}


logout  = {
    "name" : "logout",
    "help" : "Removes a publisher to the list of known publishers",
        "options" : []

}

verify_pat  = {
    "name" : "verify-pat",
    "help" : "Verifies if the Personal Access Token has publish rights for the publisher",
    "options" : [ {"action" : "store_true" , "fullFlag" : "--pat <token>" , "help" : "Personal Access Token (defaults to VSCE_PAT environment variable)" }]
    
}

show = {
    "name" : "show",
    "help" : "Shows an extension's metadata",
    "options" : [{"action" : "store_true" , "fullFlag" : "--json" , "help"  :   "Outputs data in json format (default: false)"}]

}

search = {
    "name" : "search",
    "help" : "Searches extension gallery",
    "options" : [
        {"action" : "store_true" , "fullFlag" : "--json"  , "help"   :   "Outputs data in json format (default: false)"},
        {"action" : "store_true" , "fullFlag" : "--stats" , "help"   :   "Shows extensions rating and download count (default: false)"},
        {"action" : "store_true" , "fullFlag" : "-p, --pagesize [value]"  , "help"   :   "Number of results to return (default: '100')"},        
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