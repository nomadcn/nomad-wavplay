{
    'targets': [
        {
            'target_name': '<(module_name)',
            'sources': [
                './src/main.cc',
                './src/wavplay.cc',
                './src/ext/gwutils/Flags.cpp',
                './src/ext/gwutils/Logger.cpp',
                './src/ext/gwutils/ThreadSafe.cpp',
            ],

            'include_dirs': [
                './src',
                './src/ext/gwutils'
            ],

            'conditions': [
                ['OS == "win"', {
                    'defines': [
                        'WIN32',
                        'UNICODE',
                    ],
                    'include_dirs': [
                        './src/win'
                    ],
                    'sources': [
                        './src/win/WinPlayer.cc',
                    ],
                    'libraries': ['winmm.lib'],
                    'configurations' : {
                        'Debug' : {
                            'msvs_settings': {
                                'VCCLCompilerTool': {
                                    'RuntimeLibrary': '3' # /MDd
                                },
                                'VCLinkerTool': {
                                    'AdditionalOptions': ['/ignore:4099'],
                                    'IgnoreDefaultLibraryNames': ['libcmtd.lib']
                                }
                            }
                        },
                        'Release' : {
                            'msvs_settings': {
                                'VCCLCompilerTool': {
                                    'RuntimeTypeInfo': 'true', # To disable '/GR-'
                                    'RuntimeLibrary': '2' # /MDd
                                },
                                'VCLinkerTool': {
                                    'AdditionalOptions': ['/ignore:4099'],
                                    'IgnoreDefaultLibraryNames': ['libcmt.lib']
                                }
                            }
                        }
                    }
                }],
                ['OS == "mac"', {
                    'defines': [
                        'MAC',
                        'OSX',
                    ],
                    'include_dirs': [
                        './src/mac'
                    ],
                    'sources': [
                        './src/mac/MacPlayer.cc',
                    ],
                    'xcode_settings': {
                        'GCC_ENABLE_CPP_RTTI': 'YES',
                        "OTHER_CFLAGS": [
                            "-D__MAC_OS__ -DOSX"
                        ]
                    },
                    'libraries': []
                }]
            ]
        },
        {
            "target_name": "action_after_build",
            "type": "none",
            "dependencies": [ "<(module_name)" ],
            "copies": [
                {
                    "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
                    "destination": "<(module_path)"
                }
            ]
        }
    ]
}
