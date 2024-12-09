import pymysql


def getDomainScanResults(domain):
    query = f"""
    SELECT 
        `scan_domains`.`Domain` AS domain,
        `scan_domains`.`Score` AS score,
        `scan_domains`.`HIBP` AS HIBP,
        `scan_domains`.`MALWARE` AS MALWARE,
        `scan_domains`.`OPEN_PORTS` AS OPEN_PORTS,
        `scan_domains`.`THREATFOX` AS THREATFOX,
        `scan_domains`.`VIRUSTOTAL` AS VIRUSTOTAL,
        `scan_domains`.`WAPITI` AS WAPITI,
        `scan_domains`.`CMS` AS CMS,
        `scan_domains`.`VISA` AS VISA,
        `scan_domains`.`CSA` AS CSA,
        `scan_domains`.`STATUS` AS STATUS
    FROM `websecscore`.`scan_domains`
    WHERE `Domain` = '{domain}';
    """
    try:
        db_config = {
            "host": "127.0.0.1",
            "user": "root",
            "password": "",
            "database": "websecscore",  
        }
        connection = pymysql.connect(**db_config)
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        if 'connection' in locals():
            connection.close()


def checkDomainExists(domain):
    query = f"""
    SELECT EXISTS (
        SELECT 1 
        FROM `websecscore`.`scan_domains`
        WHERE `Domain` = '{domain}'
    ) AS exists_flag;
    """
    try:
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "websecscore",  
        }
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            return bool(result[0])
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        if 'connection' in locals():
            connection.close()


# Function to insert or update scan details for a domain
def InsertUpdate(domain, scanQueryResults, companyName=None):
    score = scanQueryResults['scanScore']
    HIBP_res = scanQueryResults['scanDetails']['HIBP']
    MALWARE_res = scanQueryResults['scanDetails']['MALWARE']
    OPEN_PORTS_res = scanQueryResults['scanDetails']['OPEN_PORTS']
    THREATFOX_res = scanQueryResults['scanDetails']['THREATFOX']
    VIRUSTOTAL_res = scanQueryResults['scanDetails']['VIRUSTOTAL']
    WAPITI_res = scanQueryResults['scanDetails']['WAPITI']
    CMS_res = scanQueryResults['scanDetails']['CMS']
    STATUS = scanQueryResults.get('STATUS', 'Pending')
    visa = scanQueryResults['scanDetails'].get('VISA') if companyName else None
    csa = scanQueryResults['scanDetails'].get('CSA') if companyName else None

    query = f"""
    INSERT INTO `websecscore`.`scan_domains` (
        `Domain`, `Score`, `HIBP`, `MALWARE`, `OPEN_PORTS`, 
        `THREATFOX`, `VIRUSTOTAL`, `WAPITI`, `CMS`, `STATUS`
    """
    if companyName:
        query += ", `VISA`, `CSA`"
    query += f"""
    )
    VALUES (
        '{domain}', {score}, '{HIBP_res}', '{MALWARE_res}', '{OPEN_PORTS_res}', 
        '{THREATFOX_res}', '{VIRUSTOTAL_res}', '{WAPITI_res}', '{CMS_res}', '{STATUS}'
    """
    if companyName:
        query += f", '{visa}', '{csa}'"
    query += f"""
    )
    ON DUPLICATE KEY UPDATE
        `Score` = VALUES(`Score`),
        `HIBP` = VALUES(`HIBP`),
        `MALWARE` = VALUES(`MALWARE`),
        `OPEN_PORTS` = VALUES(`OPEN_PORTS`),
        `THREATFOX` = VALUES(`THREATFOX`),
        `VIRUSTOTAL` = VALUES(`VIRUSTOTAL`),
        `WAPITI` = VALUES(`WAPITI`),
        `CMS` = VALUES(`CMS`),
        `STATUS` = VALUES(`STATUS`)
    """
    if companyName:
        query += f""",
        `VISA` = VALUES(`VISA`),
        `CSA` = VALUES(`CSA`)
        """
    try:
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "websecscore",  
        }
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            cursor.execute(query)
        connection.commit()
        print("Command executed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'connection' in locals():
            connection.close()
