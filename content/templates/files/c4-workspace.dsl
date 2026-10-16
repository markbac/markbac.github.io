workspace "Sensor platform" "Starter C4 model" {

    model {
        installer = person "Installer" "Fits and commissions sensors."
        erp = softwareSystem "Customer ERP" "Bills customers from readings." "External"

        platform = softwareSystem "Sensor platform" "Collects readings and manages devices." {
            device = container "Sensor firmware" "Measures and reports." "C, Zephyr"
            ingest = container "Ingest service" "Receives and decodes readings." "Go"
            store = container "Time-series store" "Holds readings." "PostgreSQL" "Database"
            app = container "Installer app" "Commissions devices." "Kotlin"
        }

        installer -> app "Uses"
        app -> ingest "Registers devices with" "HTTPS"
        device -> ingest "Sends readings to" "CoAP, CBOR"
        ingest -> store "Writes readings to"
        ingest -> erp "Sends daily readings to" "HTTPS"
    }

    views {
        systemContext platform "Context" {
            include *
            autoLayout
        }
        container platform "Containers" {
            include *
            autoLayout
        }
        styles {
            element "Person" {
                shape Person
            }
            element "Database" {
                shape Cylinder
            }
            element "External" {
                background #999999
            }
        }
    }
}
