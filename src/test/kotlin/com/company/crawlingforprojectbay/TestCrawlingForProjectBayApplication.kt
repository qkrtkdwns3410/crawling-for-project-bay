package com.company.crawlingforprojectbay

import org.springframework.boot.fromApplication
import org.springframework.boot.with


fun main(args: Array<String>) {
    fromApplication<CrawlingForProjectBayApplication>().with(TestcontainersConfiguration::class).run(*args)
}
