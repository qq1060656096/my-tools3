
    function getDataProvider() {
        $data = [
    [
        'case' => '1_参数1_值1_参数2_null',
        'data' => [
            'arg1' => 'a11',
            'arg2' => null
        ],
        'expected' => [
            'has' => true
        ]
    ],
    [
        'case' => '2_参数1_值1_参数2_空字符串',
        'data' => [
            'arg1' => 'a11',
            'arg2' => ''
        ],
        'expected' => [
            'has' => true
        ]
    ],
    [
        'case' => '3_参数1_值1_参数2_值3',
        'data' => [
            'arg1' => 'a11',
            'arg2' => '21'
        ],
        'expected' => [
            'has' => true
        ]
    ],
    [
        'case' => '4_参数1_值1_参数3_值4',
        'data' => [
            'arg1' => 'a11',
            'arg2' => '22'
        ],
        'expected' => [
            'has' => true
        ]
    ],
    [
        'case' => '5_参数1_值2_参数2_null',
        'data' => [
            'arg1' => 'a12',
            'arg2' => null
        ],
        'expected' => [
            'has' => false
        ]
    ],
    [
        'case' => '6_参数1_值2_参数2_空字符串',
        'data' => [
            'arg1' => 'a12',
            'arg2' => ''
        ],
        'expected' => [
            'has' => false
        ]
    ],
    [
        'case' => '7_参数1_值2_参数2_值3',
        'data' => [
            'arg1' => 'a12',
            'arg2' => '21'
        ],
        'expected' => [
            'has' => false
        ]
    ],
    [
        'case' => '8_参数1_值2_参数3_值4',
        'data' => [
            'arg1' => 'a12',
            'arg2' => '22'
        ],
        'expected' => [
            'has' => false
        ]
    ]
];  // 直接使用 PHP 数组
        $dataNew = [];
        foreach ($data as $item) {
            $testcase = $item['case'];
            $data = $item['data'];
            $expected = $item['expected'];
            $dataNew[] = [
                $testcase,
                $data,
                $expected,
            ];
        }
        return $dataNew;
    }
    /**
     * @param string $testcase
     * @param $data
     * @param $expected
     * @return void
     * @dataProvider getDataProvider
     */
    public function testOk($testcase, $data, $expected)
    {
        $this->assertEquals(true, true, $testcase);
    }
    